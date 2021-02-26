<template>
  <li class="node-tree">
    <span class="label">{{ node.name }}</span>

    <ul v-if="node.submenu && node.submenu.length">
      <GameGeneratorTreeNode v-for="child in node.submenu" :key="child.name" :node="child" />
    </ul>
  </li>
</template>

<script>
export default {
  props: {
    node: Object
  }
};
</script>

