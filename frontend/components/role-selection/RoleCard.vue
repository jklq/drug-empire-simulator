<template>
  <div
    class="cursor-pointer bg-gray-300 rounded-sm p-4 hover:bg-gray-400"
    @mouseover="setRole({ role: type })"
    @click="postNewRole()"
  >
    <h2 class="text-3xl font-semibold">
      {{ title }}
    </h2>
    <p>
      <slot>
        Situated in Colombia, your job is to produce cocaine and pass it on to
        a broker.{{ getRole }}
      </slot>
    </p>
  </div>
</template>

<script lang="ts">
import { mapActions, mapMutations, mapGetters } from 'vuex'

export default {
  props: {
    title: {
      type: String,
      default: 'Cartel'
    },
    type: {
      type: String,
      default: 'c'
    }
  },
  computed: {
    ...mapGetters([
      'getRole'
    ])
  },
  methods: {
    ...mapActions([
      'postNewRole'
    ]),
    ...mapMutations([
      'setRole'
    ])
  }
}
</script>
