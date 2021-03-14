<script lang="ts">
import Vue from 'vue'
import { mapGetters } from 'vuex'

export default Vue.extend({
  middleware: ['loggedIn'],
  computed: {
    ...mapGetters([
      'getError',
      'getRole'
    ])
  },
  watch: {
    getRole (role) {
      if (role !== null) {
        this.$router.replace({ path: '/game' })
      }
    }
  }
})
</script>
<template>
  <div>
    <h1 class="text-2xl">Select your role!</h1>
    <div class="grid gap-8 grid-cols-3">
      <RoleCard type="c" title="Cartel">
        Situated in Colombia, your job is to produce cocaine and pass it on to a broker.
      </RoleCard>
      <RoleCard type="b" title="Broker">
        You are the middleman between the cartel and the mafia.
        Your job is to covertly transport the cocaine produced by the cartel to the mafia.
      </RoleCard>
      <RoleCard type="m" title="Mafia">
        You sell drugs and kill people who threaten your business, in Spain.
      </RoleCard>
    </div>
    <span class="error">
      {{ getError }}
    </span>
  </div>
</template>
