<script lang="ts">
import { mapActions, mapGetters } from 'vuex'

export default {
  data () {
    return {

    }
  },
  computed: {
    ...mapGetters('generator', [
      'getMenuGenerated',
      'getMenu'
    ])
  },
  methods: {
    ...mapActions('generator', [
      'fetchMenu'
    ])
  }
}
</script>
<template>
  <div>
    <button @click="fetchMenu">fetch me</button> <br>
    <button>menu generated? {{ getMenuGenerated }}</button> <br>
    <div v-if="getMenuGenerated">
      <GameGeneratorTree />
      <div v-for="menuItem in getMenu" :key="menuItem.name">
        {{ menuItem.name }}
      </div>
    </div>
    <div v-else>
      Loading...
    </div>
    <h1>hello</h1>
  </div>
</template>
