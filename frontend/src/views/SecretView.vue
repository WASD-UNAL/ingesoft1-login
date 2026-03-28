<template>
  <div class="secret-view">
    <SecretDisplay 
      v-if="phrase" 
      :secretPhrase="phrase" 
      @logout="handleLogout"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import SecretDisplay from '../components/SecretDisplay.vue';

const route = useRoute();
const router = useRouter();
const phrase = ref('');

onMounted(() => {
  const secretParam = route.params.secretPhrase;

  if (!secretParam) {
    router.push('/');
  } else {
    phrase.value = secretParam;
  }
});

const handleLogout = () => {
  router.push('/');
};
</script>