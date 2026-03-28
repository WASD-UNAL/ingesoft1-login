import axios from 'axios';


const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api',
  headers: {
    'Content-Type': 'application/json'
  }
});

export default {
  async login(correo, password) {
    try {

      const response = await apiClient.post('/login/', { correo, password });
      

      return response.data;
    } catch (error) {

      if (error.response) {
        throw error.response.data; 
      }

      throw new Error('No se pudo conectar con el servidor');
    }
  }
};
