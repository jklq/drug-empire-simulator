import config from './nuxt.config.js'

const development = config.dev || false
const API_URL_BASE = development ? 'http://localhost:5000/' : '/api/'

export { API_URL_BASE }
