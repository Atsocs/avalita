import Vue from 'vue'
import Router from 'vue-router'
import Index from '~/pages/index.vue'
import Professor from '~/pages/p/_username/index.vue'

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  routes: [
    {path: '/', component: Index, name: 'index'},
    {path: '/p/:username', component: Professor, name: 'professor'}
  ]
}

export function createRouter (ctx) {
  return new Router(routerOptions)
}
