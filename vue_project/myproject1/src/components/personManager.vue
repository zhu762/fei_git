<template>
<div>
    <div class="control">
        <Button type="primary" @click="personManagerModalShow(0,'add')">Add</Button>
    </div>
    <Modal
        v-model="personManagerModal"
        title="personManager"
        @on-ok="personAdd"
        :mask-closable="false">
        <Input v-model="person.name"><span slot="prepend">Name</span></Input>
        <Input v-model="person.age"><span slot="prepend">Age</span></Input>
        <Input v-model="person.address"><span slot="prepend">Address</span></Input>
    </Modal>
    <Table border :columns="personColumns" :data="personData"></Table>
</div>
</template>

<script>
var personInfo={
    name:"",
    age:"",
    address:"",
}
export default {
    data() {
        return {
            personManagerModal: false,
            person: {},
            personColumns: [
                    {
                        title: 'Name',
                        key: 'name'
                    },
                    {
                        title: 'Age',
                        key: 'age'
                    },
                    {
                        title: 'Address',
                        key: 'address'
                    },
                    {
                        title: 'DateTime',
                        key: 'datetime'
                    },
                    {
                        title: 'Action',
                        key: 'action',
                        width: 200,
                        align: 'center',
                        render: (h, params) => {
                            return h('div', [
                                h('Button', {
                                    props: {
                                        type: 'success',
                                        size: 'small'
                                    },
                                    style: {
                                        marginRight: '5px'
                                    },
                                    on: {
                                        click: () => {
                                            this.personManagerModalShow(params.index,'update')
                                        }
                                    }
                                }, 'Update'),
                                h('Button', {
                                    props: {
                                        type: 'error',
                                        size: 'small'
                                    },
                                    on: {
                                        click: () => {
                                            this.personDel(params.index)
                                        }
                                    }
                                }, 'Delete')
                            ]);
                        }
                    }
                ],
                personData: [],
                updateflag: {
                    action:'',
                    index:''
                }
        }
    },
    mounted: function(){
        this.getPersons()
    },
    methods: {
        getPersons(){
            this.axios.get("http://127.0.0.1:8000/pyfei/person")
            .then((resp) => {
                resp.data.persons.forEach(element => {
                    this.personData.push({
                        id:element.id,
                        name:element.name,
                        age:element.age,
                        address:element.address,
                        datetime:element.datetime
                    })
                });
            })
            .catch((error) => {
                console.log(error);
            });
        },
        personManagerModalShow(index,action){
            this.updateflag.index = index
            this.updateflag.action = action
            if(action=="add"){
                this.person = JSON.parse(JSON.stringify(personInfo))
            }else{
                this.person = JSON.parse(JSON.stringify(this.personData[index]))
            }
            this.personManagerModal = true
        },
        personAdd(){
            if(this.person.name==""||this.person.age==""||this.person.address==""){
                alert("数据不能为空")
                return
            }
            this.axios.post("http://127.0.0.1:8000/pyfei/person",JSON.stringify({person:this.person,action:this.updateflag.action}),{headers:{"Content-Type": "application/json"}})
            .then((resp) => {
                if(resp.data.code==200){
                    if(this.updateflag.action=="add"){
                        this.personData.unshift(resp.data.person)
                        this.$Message.success("新增成功")
                    }else{
                        this.$set(this.personData,this.updateflag.index,resp.data.person)
                        this.$Message.success("更新成功")
                    }
                }else{
                    this.$Message.error("失败")
                }
            })
            .catch((error) => {
                console.log(error);
            });
        },
        personDel(index){
            this.axios.post("http://127.0.0.1:8000/pyfei/personDel",JSON.stringify({id:this.personData[index].id}),{headers:{"Content-Type": "application/json"}})
            .then((resp) => {
                if(resp.data.code==200){
                    this.personData.splice(index,1)
                    this.$Message.success("删除人员成功")
                }else{
                    this.$Message.error("删除人员失败")
                }
            })
            .catch((error) => {
                console.log(error);
            });
        }
    },
    components: {

    }
}
</script>

<style scoped>
.control{
    margin: 15px;
    padding: 15px;
    border: 1px solid #dcdee2;
    border-radius: 5px;
}
</style>
