<template>
  <div>
    <div>
      <label for="email" class="block">Email:</label>
      <BaseInput id="email" v-model="email" type="text" />
    </div>
    <div>
      <label for="password" class="block">Password</label>
      <BaseInput id="password" type="password" />
    </div>
    <span @click="authUser">
      <BaseButton el="button" class="inline-block mt-2">
        Logg inn
      </BaseButton>
    </span>
    <button @click="authUser">testButton</button>
    {{ response }}
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default Vue.extend({
  data () {
    return {
      email: 'test'
    }
  },
  computed: {
    ...mapGetters('user', [
      'response'
    ])
  },
  methods: {
    ...mapActions({
      authUser: 'user/authUser'
    }),
    ...mapMutations({
      increment: 'user/increment'
    })
  }

})
</script>
