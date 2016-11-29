var Vue = require('vue')
var Vuex = require('vuex')
Vue.use(Vuex)
var Example = require('./vue/SubscribeForm.vue')

const store = new Vuex.Store({
  state: {
    regions: []
  },
  mutations: {
    setResgions(state, regions) {
      state.regions = regions
    }
  },
  actions: {
    getData(context) {
      fetch('/regions.json').then(function(response) {
          return response.json().then(function(json) {
            context.commit('setResgions', json)
          },
          () => context.commit('setResgions', {})
        );
      });
    }
  }
})

new Vue({
  el: '#app',
  store,
  render: h => h(Example)
})

store.dispatch('getData')
