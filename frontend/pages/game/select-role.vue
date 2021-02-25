<script lang="ts">
import Vue from 'vue'
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default Vue.extend({
  mounted () {
    const loggedIn = this.$store.dispatch('user/isLoggedIn')
    if (loggedIn) {
      console.log("redirect")
      this.$router.push('/login')
    }
  }
})
</script>
<template>
  <div>
    <h1 class="text-2xl">Select your role!</h1>
    <div class="grid gap-8 grid-cols-3">
      <RoleCard title="Cartel">
        Situated in Colombia, your job is to produce cocaine and pass it on to a broker.
      </RoleCard>
      <RoleCard title="Broker">
        You are the middleman between the cartel and the mafia.
        Your job is to covertly transport the cocaine produced by the cartel to the mafia.
      </RoleCard>
      <RoleCard title="Mafia">
        You sell drugs and kill people who threaten your business, in Spain.
      </RoleCard>
    </div>
  </div>
</template>
