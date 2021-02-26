<template>
  <div class="tree bg-red-400">
    <ul class="tree-list">
      <div v-for="menuItem in getMenu" :key="menuItem.name">
        <GameGeneratorTreeNode :node="menuItem" />
      </div>
    </ul>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  computed: {
    ...mapGetters('generator', [
      'getMenu'
    ])
  }
}
</script>

<style>
.tree-list ul {
  padding-left: 16px;
  margin: 6px 0;
}
</style>
