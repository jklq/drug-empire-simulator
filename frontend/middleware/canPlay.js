import { API_URL_BASE } from '../config.js'

export default async (context) => {
  return context.$axios.get(API_URL_BASE + 'user/profile/can-play/').then((res) => {
    if (!res.data.result) {
      return context.redirect(res.data.redirectUrl)
    }
  }).catch((error) => {
    return context.redirect(error.response.data.redirectUrl)
  })
}
