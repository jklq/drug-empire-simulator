import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import cookies from 'browser-cookies'

import { API_URL_BASE } from '../config.js'

Vue.use(Vuex)

export const state = () => ({
  menuGenerated: false,
  menu: null
})

export const getters = {
  getMenuGenerated (state) {
    return state.menuGenerated
  },
  getMenu (state) {
    return state.menu
  }
}

export const mutations = {
  menuIsGenerated (state, { menu }) {
    state.menuGenerated = true
    state.menu = menu
  }
}

export const actions = {
  fetchMenu ({ commit }) {
    axios.get(API_URL_BASE + 'game/generator/').then(res => {
      commit('menuIsGenerated', { menu: res.data })
      return res.data
    })
  }
}
