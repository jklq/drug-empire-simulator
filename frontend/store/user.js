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
  email: 'test',
  password: 'test',
  loggedIn: false,
  authToken: null,
  counter: 0,
  errorMsg: 'test'
})

export const mutations = {
  logUserIn (state, { token }) {
    state.loggedIn = true
    state.authToken = token
  },
  setError (state, payload) {
    state.errorMsg = payload.msg
  },
  setEmail (state, username) {
    console.log("username: " + username)
    console.log("username state: " + state.username)
    state.username = username
  },
  setPassword (state, password) {
    state.username = password
  }
}
export const getters = {
  authToken (state) {
    return state.authToken
  },
  errorMsg (state) {
    return state.errorMsg
  },
  getEmail (state) {
    return state.email
  }
}
export const actions = {
  handleError (state, { status }) {
    let msg
    switch (status) {
      case 400:
        msg = 'Invalid'
        break
      default:
        msg = 'unexpected error'
        break
    }
    state.commit('setError', { msg })
  },
  authUser ({ commit, dispatch }, user) {
    console.log(user)
    axios.post(API_URL_BASE + 'user/login/', {
      email: user.email,
      password: user.password
    }).then((res) => {
      commit('logUserIn', { token: res.data.msg })
      cookies.set('token', res.data.msg, { expires: 2.7 })
    }).catch((error) => {
      console.log(error.response)
      dispatch('handleError', { status: error.response.status })
    })
  }
}
