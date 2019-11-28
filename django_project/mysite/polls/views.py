from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader,RequestContext
from .models import Question
import json

# Create your views here.

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    # # 1.获取模板
    # template = loader.get_template('polls/index.html')
    # # 2.定义上下文
    # context = {'title': '投票', 'list': range(10)}
    # # 3.渲染模板
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', {'title': '投票', 'list': range(10)})

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def getlist(request):
    headers = {
        "Access-Control-Allow-Origin": "*"
    }
    response = JsonResponse([1,2,3,4,5,6,7,8,9], safe=False)
    # response["Access-Control-Allow-Origin"] = "*"
    # response["Access-Control-Allow -Headers"] = "*"
    return response