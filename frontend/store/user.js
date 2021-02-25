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
  username: 'username',
  loggedIn: false,
  authToken: null,
  counter: 0,
  errorMsg: ''
})

export const mutations = {
  logUserIn (state, { token }) {
    state.loggedIn = true
    state.authToken = token
  },
  setError (state, payload) {
    state.errorMsg = payload.msg
  },
  setEmail (state, email) {
    state.email = email
  },
  setPassword (state, password) {
    state.password = password
  },
  setUsername (state, username) {
    state.username = username
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
  },
  getPassword (state) {
    return state.password
  },
  getUsername (state) {
    return state.username
  }
}
export const actions = {
  handleError (state, { response }) {
    let msg
    /*
    switch (status) {
      case 400:
        msg = 'Invalid input details'
        break
      case 401:
        msg = 'Wrong username or password'
        break
      case 409:
        msg = 'Wrong username or password'
        break
      default:
        msg = 'Unexpected error'
        break
    } */
    state.commit('setError', { msg: response.data.msg })
  },
  authUser ({ commit, dispatch, getters, redirect }) {
    commit('setError', { msg: '' })
    axios.post(API_URL_BASE + 'user/login/', {
      email: getters.getEmail,
      password: getters.getPassword
    }).then((res) => {
      commit('logUserIn', { token: res.data.msg })
      cookies.set('token', res.data.msg, { expires: 2.7 })
      cookies.set('loggedIn', 'true', { expires: 2.7 })
      this.$router.replace({ path: '/game/select-role' })
    }).catch((error) => {
      console.log(error)
      console.log(error.response)
      dispatch('handleError', { response: error.response })
    })
  },
  registerUser ({ commit, dispatch, getters }) {
    commit('setError', { msg: '' })
    axios.post(API_URL_BASE + 'user/register/', {
      username: getters.getUsername,
      email: getters.getEmail,
      password: getters.getPassword
    }).then((res) => {
      dispatch('authUser')
    }).catch((error) => {
      console.log(error.response)
      dispatch('handleError', { response: error.response })
    })
  }
}
