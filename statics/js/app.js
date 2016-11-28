var Vue = require('vue')
var Vuex = require('vuex')
Vue.use(Vuex)
var Example = require('./vue/SubscribeForm.vue')

const store = new Vuex.Store({
  state: {
    ajax_data: ""
  },
  mutations: {
    showBackendValue(state, a_text) {
      state.ajax_data = a_text
    }
  },
  actions: {
    getData(context) {
      fetch('/regions.json').then(function(response) {
          return response.json().then(function(json) {
            console.log(json);
            context.commit('showBackendValue', 'got it')
          },
          () => context.commit('showBackendValue', "Error")
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
