<template>
  <div class="login-form-wrapper">
    <form @submit.prevent="handleSubmit" class="login-form">
      <h2>Iniciar Sesión</h2>
      
      <div class="input-group">
        <label for="correo">Correo</label>
        <input 
          type="email" 
          id="correo" 
          v-model="correo" 
          required 
          placeholder="tu@correo.com"
        />
      </div>

      <div class="input-group">
        <label for="password">Contraseña</label>
        <input 
          type="password" 
          id="password" 
          v-model="password" 
          required 
          placeholder="********"
        />
      </div>

      <div v-if="errorMessage" class="error-message">
        {{ errorMessage }}
      </div>

      <button type="submit" :disabled="loading" class="submit-btn">
        {{ loading ? 'Ingresando...' : 'Entrar' }}
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import authService from '../services/authService';

const emit = defineEmits(['login-success']);

const correo = ref('');
const password = ref('');
const loading = ref(false);
const errorMessage = ref('');

const handleSubmit = async () => {
  loading.value = true;
  errorMessage.value = '';

  try {
    const response = await authService.login(correo.value, password.value);
    console.log('Respuesta del backend:', response);
    emit('login-success', response.secretPhrase);
    
  } catch (error) {
    errorMessage.value = error.message || 'Credenciales inválidas, intenta de nuevo.';
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
.login-form {
  background-color: #ffffff;
  padding: 2.5rem;
  border-radius: 12px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
  width: 100%;
  max-width: 400px;
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}

h2 {
  text-align: center;
  color: #333;
  margin-bottom: 1rem;
}

.input-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

label {
  font-weight: 600;
  font-size: 0.9rem;
  color: #555;
}

input {
  padding: 0.8rem;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 1rem;
  background-color: #333;
  color: #ddd;
  transition: all 0.3s ease;
}


input:focus {
  outline: none;
  border-color: #0d9488;
  box-shadow: 0 0 0 2px rgba(13, 148, 136, 0.2);
}


input::placeholder {
  color: #a0a0a0;
}


.submit-btn {
  background: linear-gradient(135deg, #66d7d1 0%, #0d9488 100%); /* Nuevo degradado de botón */
  color: white;
  padding: 1rem;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: opacity 0.3s ease;
  margin-top: 1rem;
}

.submit-btn:hover:not(:disabled) {
  opacity: 0.9;
}

.submit-btn:disabled {
  background: #a0a0a0;
  cursor: not-allowed;
}

.error-message {
  background-color: #fecdd3; 
  color: #e11d48; 
  padding: 0.8rem;
  border-radius: 6px;
  font-size: 0.9rem;
  text-align: center;
  border: 1px solid #f9a8d4;
}
</style>