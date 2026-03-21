<template>
    <div class="container">
        <form class="form" @submit.prevent="handleSubmit">
            <div class="form-header">
                <h2>Bienvenido</h2>
                <p>Ingresa tus datos para continuar</p>
            </div>
            <input class="form-input" type="email" placeholder="Correo electrónico" v-model="correo" required/>
            <input class="form-input" type="password" placeholder="Contraseña" v-model="password" required/>
            <div v-if="errorMessage" class="error-message">   
                {{ errorMessage }}
            </div>
            <button class="submit-button" type="submit" :disabled="loading">
                {{ loading ? "Ingresando..." : "Ingresar" }}
            </button>
        </form>
    </div>
</template>

<script>
    import AuthService from "../services/AuthService"
    export default{
        name: "LoginForm",
        data(){
            return{
                correo:"",
                password:"",
                loading:false,
                errorMessage:""
            };
        },
        methods:{
            async handleSubmit(){
                this.loading=true;
                this.errorMessage="";
                try{
                    const response = await AuthService.login(this.correo,this.password)
                        if(response.status === 200 && response.data.success){
                            this.$emit("login-success",response.data.secret_phrase)
                        }
                }catch(error){
                    if (error.response && error.response.data) {
                        this.errorMessage = error.response.data.message
                    } else {
                        this.errorMessage = "Error al intentar iniciar sesión"
                    }
                } finally{
                    this.loading=false
                }
            }
        }
    }
</script>

<style scoped>
.container {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background: var(--primary-gradient);
    padding: 20px;
}

.form {
    background-color: var(--white);
    padding: 48px 40px;
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-lg);
    display: flex;
    flex-direction: column;
    gap: 24px;
    width: 100%;
    max-width: 450px;
    box-sizing: border-box;
}

.form-header {
    text-align: center;
    margin-bottom: 8px;
}

.form-header h2 {
    margin: 0 0 8px 0;
    color: var(--text-main);
    font-size: 28px;
    font-weight: 700;
}

.form-header p {
    margin: 0;
    color: var(--text-muted);
    font-size: 15px;
}

.form-input {
    padding: 16px;
    border: 1.5px solid var(--border-light);
    border-radius: var(--radius-md);
    font-size: 15px;
    color: var(--text-main);
    background-color: var(--bg-color);
    transition: all 0.25s ease;
    outline: none;
    font-family: inherit;
    box-sizing: border-box;
}

.form-input::placeholder {
    color: var(--text-muted);
}

.form-input:focus {
    border-color: #42b983;
    background-color: var(--white);
    box-shadow: var(--focus-ring);
}

.submit-button {
    background: var(--button-gradient);
    color: var(--white);
    padding: 16px;
    border: none;
    border-radius: var(--radius-md);
    font-size: 16px;
    font-weight: 600;
    letter-spacing: 0.3px;
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.2s ease, background-color 0.2s ease;
    margin-top: 8px;
    font-family: inherit;
    box-sizing: border-box;
}

.submit-button:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}

.submit-button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
    transform: none;
    box-shadow: none;
}

.error-message {
    background-color: var(--error-bg);
    color: var(--error-text);
    padding: 14px;
    border-radius: var(--radius-md);
    font-size: 14px;
    font-weight: 500;
    text-align: center;
    border: 1px solid var(--error-border);
    display: flex;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
}
</style>
