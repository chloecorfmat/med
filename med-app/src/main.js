import Vue from 'vue'
import VueSession from 'vue-session'
import moment from 'moment'


import App from './App.vue'
import router from './router'

Vue.config.productionTip = false
Vue.use(VueSession)

Vue.filter('formatDate', function(value, format) {
  if (value) {
    moment.locale('fr')
    return moment(String(value)).format(format)
  }
})

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
