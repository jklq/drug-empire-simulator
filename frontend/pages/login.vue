<template>
  <div>
    <div>
      <label for="email" class="block">Email:</label>
      <BaseInput id="email" v-model="email" type="text" />
      <input v-model="email">
    </div>
    <div>
      <label for="password" class="block">Password</label>
      <BaseInput id="password" v-model="password" type="password" />
    </div>
    <span @click="authUser({email: email, password: password})">
      <BaseButton el="button" class="inline-block mt-2">
        Logg inn
      </BaseButton>
    </span>
    <button @click="authUser()">testButton</button>
    {{ errorMsg }}
    {{ authToken }}
    <h2>VARS</h2>
    email: {{ getEmail }} <br>

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
