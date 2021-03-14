import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

import { API_URL_BASE } from '../config.js'

Vue.use(Vuex)

export const state = () => ({
  role: null,
  errorMsg: null
})

export const mutations = {
  setRole (state, payload) { state.role = payload.role },
  setError (state, payload) { state.errorMsg = payload.msg }
}
export const getters = {
  getRole (state) {
    return state.role
  },
  getError (state) {
    return state.errorMsg
  }
}
export const actions = {
  postNewRole (context) {
    console.log(context.getters.getRole)
    const token = this.$cookiz.get('token')
    axios.defaults.headers.common.Authorization = 'Bearer ' + token // for all requests
    axios.post(API_URL_BASE + 'user/profile/select-role/', {
      role: context.getters.getRole
    }).then((res) => {
      this.$router.replace({ path: '/game/' })
    }).catch((error) => {
      const errorMsg = error.response.data.msg
      if (errorMsg.includes('Already')) {
        this.$router.replace({ path: '/game/' })
      } else {
        context.commit('setError', { msg: errorMsg })
      }

    })
  }
}
