<template>
  <div class="secret-container">
    <div class="secret-card">
      <div class="icon-check">✓</div>
      <h1>¡Login Exitoso!</h1>
      
      <p class="instruction">Esta es tu frase secreta guardada en el servidor:</p>
      
      <div class="phrase-box">
        {{ secretPhrase }}
      </div>

      <button @click="handleLogout" class="logout-btn">
        Cerrar Sesión
      </button>
    </div>
  </div>
</template>

<script setup>

defineProps({
  secretPhrase: {
    type: String,
    required: true
  }
});


const emit = defineEmits(['logout']);

const handleLogout = () => {
  emit('logout');
};
</script>

<style scoped>

.secret-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
  padding: 20px;
}


.secret-card {
  background: white;
  padding: 3rem;
  border-radius: 20px;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
  text-align: center;
  max-width: 450px;
  width: 100%;
}

.icon-check {
  font-size: 4rem;
  color: #2ecc71;
  margin-bottom: 1rem;
}

h1 {
  color: #2c3e50;
  margin-bottom: 1rem;
}

.instruction {
  color: #7f8c8d;
  margin-bottom: 1.5rem;
}


.phrase-box {
  background-color: #f9f9f9;
  border: 2px dashed #2ecc71;
  padding: 1.5rem;
  font-size: 1.2rem;
  font-weight: bold;
  color: #27ae60;
  border-radius: 10px;
  margin-bottom: 2rem;
  word-break: break-all;
}


.logout-btn {
  background-color: #ecf0f1;
  color: #7f8c8d;
  border: none;
  padding: 0.8rem 2rem;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
}

.logout-btn:hover {
  background-color: #e74c3c;
  color: white;
}
</style>