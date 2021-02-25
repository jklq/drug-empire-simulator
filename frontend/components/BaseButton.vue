<script lang="ts">
export default {
  props: {
    el: {
      type: String,
      default: 'router-link'
    },
    link: {
      type: String,
      default: ''
    },
    type: {
      type: String,
      default: 'default'
    }
  },
  data () {
    return {
    }
  }
}
</script>
<template>
  <NuxtLink
    :is="el"
    :to="link"
    class="btn-base"
    :class="['btn-' + type]"
  >
    <slot />
  </NuxtLink>
</template>
<style>
.btn-base {
 @apply border-2;
}
.btn-primary {
  @apply p-2 border-gray-800 bg-gray-800 text-white;
}
.btn-default {
  @apply p-2 border-gray-800;
}
</style>
