<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  layout: 'game',
  middleware: 'loggedIn'
})
</script>
<template>
  <div>
    <GameMenuGenerator></GameMenuGenerator>
  </div>
</template>
