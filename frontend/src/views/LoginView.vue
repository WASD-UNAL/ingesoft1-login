<template>
  <div class="login-view-container">
    <LoginForm @login-success="goToSecret" />
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import LoginForm from '../components/LoginForm.vue';


const router = useRouter();

const goToSecret = (phrase) => {
  router.push({ 
    name: 'Secret', 
    params: { secretPhrase: phrase } 
  });
};
</script>

<style scoped>
.login-view-container {
  width: 100%;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, #0a3d16 0%, #0c8c9b 100%);
}
</style>
