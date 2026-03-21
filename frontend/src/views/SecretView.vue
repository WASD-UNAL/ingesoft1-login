<template>
  <div>
    <SecretDisplay :secretPhrase="secretPhrase" @logout="handleLogout"/>
  </div>
</template>

<script>
import SecretDisplay from "../components/SecretDisplay.vue"

export default {
  name: "SecretView",
  components: {
    SecretDisplay
  },
  data() {
    return {
      secretPhrase: ""
    }
  },
  created() {
    this.secretPhrase = this.$route.params.secretPhrase

    if (!this.secretPhrase) {
      this.$router.push({ name: "Login" })
    }
  },
  methods: {
    handleLogout() {
      this.$router.push({ name: "Login" })
    }
  }
}
</script>