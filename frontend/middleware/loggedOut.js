export default async (context) => {
  const cookies = context.app.$cookiz

  const loggedIn = cookies.get('loggedIn')
  if (loggedIn) {
    return context.redirect('/game')
  }
}
