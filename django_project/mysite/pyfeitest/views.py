from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from dbutils import MyPymysql
import json
import datetime

# Create your views here.


class Index(View):
    def get(self, request):
        with MyPymysql() as c:
            c.execute("SELECT * FROM polls_question")
            ret = c.fetchone()
        print(ret)
        return HttpResponse(ret)

    def post(self, request):
        pass

class Person(View):
    def get(self, request):
        with MyPymysql() as c:
            c.execute("select * from persons order by id desc")
            dbpersons = c.fetchall()
        persons = []
        for dbid, name, age, address, dbdatetime in dbpersons:
            dbdatetime = dbdatetime.strftime("%Y-%m-%d %H:%M:%S")
            persons.append(dict(id=dbid, name=name, age=age, address=address, datetime=dbdatetime))
        return JsonResponse({"code":200,"persons":persons}, safe=False)

    def post(self, request):
        dataRequest= json.loads(request.body.decode())
        person = dataRequest.get("person")
        name = person.get("name")
        age = person.get("age")
        address = person.get("address")
        action = dataRequest.get("action")
        with MyPymysql() as c:
            if action == "update":
                dbid = person.get("id")
                row = c.execute("update persons set name=%s,age=%s,address=%s where id=%s", (name, age, address, dbid))
                lastid = dbid
            else:
                row = c.execute("insert into persons (name,age,address) values (%s,%s,%s)", (name, age, address))
                lastid = c.lastrowid
            if row > 0:
                c.execute("select * from persons where id=%s", lastid)
                personNew = c.fetchall()
                for dbid, name, age, address, dbdatetime in personNew:
                    dbdatetime = dbdatetime.strftime("%Y-%m-%d %H:%M:%S")
                    return JsonResponse({"code": 200, "person": dict(id=dbid, name=name, age=age, address=address, datetime=dbdatetime)}, safe=False)
        return JsonResponse({"code": -1}, safe=False)

class personDel(View):
    def post(self, request):
        dataRequest = json.loads(request.body.decode())
        dbid = dataRequest.get("id")
        with MyPymysql() as c:
            row = c.execute("delete from persons where id=%s", dbid)
            if row > 0:
                return JsonResponse({"code": 200}, safe=False)
        return JsonResponse({"code": -1}, safe=False)


