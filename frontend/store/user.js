import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import cookies from 'browser-cookies'

import config from '../nuxt.config.js'
const development = config.dev || false

let API_URL_BASE = '/'

if (development) {
  API_URL_BASE = 'http://localhost:5000/'
} else {
  API_URL_BASE = '/api/'
}

Vue.use(Vuex)

export const state = () => ({
  loggedIn: false,
  authToken: null,
  counter: 0,
  response: 'Nothing yet!'
})

export const mutations = {
  logUserIn (state, { token }) {
    state.loggedIn = true
    state.authToken = token
  }
}
export const getters = {
  response (state) {
    return state.authToken
  }
}
export const actions = {
  authUser ({ commit }) {
    axios.post(API_URL_BASE + 'user/login/', {
      email: 'email',
      password: 'password'
    }).then((res) => {
      commit('logUserIn', { token: res.data.msg })
      cookies.set('token', res.data.msg, { expires: 2.7 })
    })
  }
}
