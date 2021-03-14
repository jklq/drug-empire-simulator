export default async (context) => {
  const cookies = context.app.$cookiz

  const loggedIn = cookies.get('loggedIn')
  console.log('loggedIn: ' + loggedIn)
  if (!loggedIn) {
    return context.redirect('/login')
  }
  const token = cookies.get('token')
  context.$axios.defaults.headers.common.Authorization = 'Bearer ' + token // for all requests
  return false
}
