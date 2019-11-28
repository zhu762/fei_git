<template>
<div>
    <div class="topBox">
        <div class="panel panel-default">
        <div class="panel-body">
            Basic panel example
        </div>
        </div>
        <Divider />
        <Menu mode="horizontal" active-name="1">
            <MenuItem name="1" to="/">
                首页
            </MenuItem>
            <MenuItem name="2" to="/personManager">
                人员管理
            </MenuItem>
        </Menu>
    </div>
    
    <div class="main">
        <router-view></router-view>
    </div>
</div>
</template>

<script>
export default {
    data () {
        return {

        }
    },
    mounted: function(){

    },
    methods: {
       
    },
    components: {

    }
}
</script>

<style scoped>
a{text-decoration:none;}
.topBox{
    background-color: #f8f8f9;
    padding-top: 2%;
}
.panel{
    margin: 0 2% 2%;
}
.ivu-divider-horizontal{
    margin: 0;
}
</style>
