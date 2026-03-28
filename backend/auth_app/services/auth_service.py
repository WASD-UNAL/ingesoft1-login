import hashlib
from auth_app.repositories import user_repository
class AuthService:
    
    def hash_password(password):
        sha512 = hashlib.sha512()
        sha512.update(password.encode('utf-8'))
        return sha512.hexdigest()

    
    def authenticate(correo, password):
        try:
            user = user_repository.find_by_correo(correo)
            if not user:
                return {"success": False, "message": "Usuario no encontrado"}
            hashed_input_password = AuthService.hash_password(password)
            if hashed_input_password == user.password_hash:
                return {"success": True, "message": "Autenticación exitosa" ,"secretPhrase": user.secret_phrase}
            return {"success": False, "message": "Contraseña incorrecta"}
        except Exception as e:
            return {"success": False, "message": "Error durante la autenticación"}
        
    
    def register(correo, password, secret_phrase):
        try:
            existing_user = user_repository.find_by_correo(correo)
            if existing_user:
                return {"success": False, "message": "Correo ya registrado"}
            password_hash = AuthService.hash_password(password)
            user_repository.create_user(correo, password_hash, secret_phrase)
            return {"success": True, "message": "Registro exitoso"}
        except Exception as e:
            return {"success": False, "message": "Error durante el registro"}