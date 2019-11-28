import Vue from 'vue'
import Router from 'vue-router'
import index from '@/components/index'
import personManager from '@/components/personManager'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      component: index,
      children: [
          {
            path: '/personManager',
            component: personManager,
          }
      ]
    }
  ]
})
