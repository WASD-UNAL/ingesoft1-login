<template>
    <div class="success-container">
        <div class="card">
            <div class="icon">✓</div>
            <h2>¡Login Exitoso!</h2>
            <div class="secret-box">{{ secretPhrase }}</div>
            <button @click="handleLogout">Cerrar sesión</button>
        </div>
    </div>
</template>

<script>
    export default{
        name:"SecretDisplay",
        props:{
            secretPhrase:{
                type:String,
                required: true
            }
        },
        methods:{
            handleLogout(){
                this.$emit("logout")
            }
        }
    }
</script>

<style scoped>
.success-container {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background: var(--success-gradient);
    padding: 20px;
}

.card {
    background-color: var(--white);
    padding: 48px 40px;
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-lg);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 24px;
    width: 100%;
    max-width: 450px;
    text-align: center;
    box-sizing: border-box;
}

.icon {
    background-color: var(--success-bg);
    color: var(--success-text);
    width: 64px;
    height: 64px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 32px;
    font-weight: 700;
}

h2 {
    margin: 0;
    color: var(--text-main);
    font-size: 28px;
    font-weight: 700;
}

.secret-box {
    background-color: var(--bg-color);
    padding: 24px;
    border: var(--border-dashed);
    border-radius: var(--radius-md);
    font-size: 16px;
    color: var(--text-main);
    letter-spacing: 0.5px;
    word-break: break-all;
    width: 100%;
    box-sizing: border-box;
    font-weight: 500;
}

button {
    background-color: transparent;
    color: var(--text-muted);
    padding: 16px;
    border: 1.5px solid var(--border-light);
    border-radius: var(--radius-md);
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.25s ease;
    width: 100%;
    font-family: inherit;
    margin-top: 8px;
}

button:hover {
    color: var(--text-main);
    border-color: var(--text-muted);
    background-color: var(--bg-color);
}
</style>