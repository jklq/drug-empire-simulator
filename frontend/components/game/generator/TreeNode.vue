<script>
import { mapActions } from 'vuex'

export default {
  props: {
    node: Object
  },
  methods: {
    ...mapActions('generator', [
      'post'
    ])
  }
}
</script>

<template>
  <li class="node-tree">
    <span
      v-if="!node.type || node.type == 'drawer'"
      class="cursor-pointer label"
      @click="node.folded = !node.folded"
    >
      {{ node.name }}
    </span>
    <button
      class="label p-2 rounded-sm bg-green-200 m-2 hover:bg-green-300 duration-100"
      v-if="node.type == 'action'"
      @click="post({ url: node.action })"
    >
      Action: {{ node.name }}: {{ typeof node.action }}
    </button>

    <ul v-if="node.submenu && node.submenu.length && typeof node.folded !== 'undefined' && !node.folded">
      <GameGeneratorTreeNode v-for="child in node.submenu" :key="child.name" :node="child" />
    </ul>
  </li>
</template>

