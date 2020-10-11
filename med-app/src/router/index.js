import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/day/:date',
    name: 'Day',
    component: () => import('../views/Day.vue'),
    props: true
  },
  {
    path: '/logout',
    name: 'Logout',
    component: () => import('../views/Logout.vue')
  }
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  if (to.name !== 'Login' && !Vue.prototype.$session.has('token')) next({ name: 'Login' })
  if (to.name === 'Login' && Vue.prototype.$session.has('token')) next({ name: 'Home' })
  else next()
})

export default router
