<script lang="ts">
export default {
  props: {
    title: {
      type: String,
      default: 'Cartel'
    }
  }
}
</script>
<template>
  <div class="bg-gray-300 rounded-sm p-4 hover:bg-gray-400">
    <h2 class="text-3xl font-semibold">{{ title }}</h2>
    <p><slot>Situated in Colombia, your job is to produce cocaine and pass it on to
    a broker.</slot></p>
  </div>
</template>
