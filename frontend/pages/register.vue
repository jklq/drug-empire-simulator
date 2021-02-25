<template>
  <div>
    <div>
      <label for="username" class="block">Username:</label>
      <input
        id="username"
        v-model="username"
        type="text"
        class="border-2 p-2 text-lg border-gray-800"
        @keydown.enter="registerUser()"
      >
    </div>
    <div>
      <label for="email" class="block">Email:</label>
      <input
        id="email"
        v-model="email"
        type="text"
        class="border-2 p-2 text-lg border-gray-800"
        @keydown.enter="registerUser()"
      >
    </div>
    <div>
      <label for="password" class="block">Password</label>
      <input
        id="password"
        v-model="password"
        type="password"
        class="border-2 p-2 text-lg border-gray-800"
        @keydown.enter="registerUser()"
      >
    </div>
    <span @click="registerUser()">
      <BaseButton el="button" class="inline-block mt-2">
        Logg inn
      </BaseButton>
    </span>
    <span class="text-red-600 block">{{ errorMsg }}</span>
  </div>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapGetters, mapMutations, mapActions } from 'vuex'

export default Vue.extend({
  data () {
    return {
    }
  },
  computed: {
    ...mapGetters('user', [
      'authToken',
      'errorMsg',
      'getEmail'
    ]),
    email: {
      get () {
        return this.$store.state.user.email
      },
      set (value) {
        this.$store.commit('user/setEmail', value)
      }
    },
    password: {
      get () {
        return this.$store.state.user.password
      },
      set (value) {
        this.$store.commit('user/setPassword', value)
      }
    },
    username: {
      get () {
        return this.$store.state.user.username
      },
      set (value) {
        this.$store.commit('user/setUsername', value)
      }
    }
  },
  methods: {
    ...mapActions({
      registerUser: 'user/registerUser'
    }),
    ...mapMutations({
      increment: 'user/increment'
    })
  }

})
</script>
