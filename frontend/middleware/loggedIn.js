export default async (context) => {
  const cookies = context.app.$cookiz

  const loggedIn = cookies.get('loggedIn')
  console.log('loggedIn: ' + loggedIn)
  if (!loggedIn) {
    return context.redirect('/login')
  }
  return false
}
