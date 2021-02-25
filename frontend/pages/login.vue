<template>
  <div>
    <div>
      <label for="email" class="block">Email:</label>
      <input
        id="email"
        v-model="email"
        type="text"
        class="border-2 p-2 text-lg border-gray-800"
        @keydown.enter="authUser()"
      >
    </div>
    <div>
      <label for="password" class="block">Password</label>
      <input
        id="password"
        v-model="password"
        type="password"
        class="border-2 p-2 text-lg border-gray-800"
        @keydown.enter="authUser()"
      >
    </div>
    <span @click="authUser()">
      <BaseButton el="button" class="inline-block mt-2">
        Logg inn
      </BaseButton>
    </span>
    <button @click="authUser()">
      testButton
    </button>
    <span class="text-red-600 block">{{ errorMsg }}</span>
    {{ authToken }}
    <h2>VARS</h2>
    email: {{ email }} <br>

    password: {{ password }}
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
    }
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
