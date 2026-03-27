import hashlib
from auth_app.repositories.user_repository import UserRepository
class AuthService:
    @staticmethod
    def hash_password(password):
        sha512 = hashlib.sha512()
        sha512.update(password.encode('utf-8'))
        return sha512.hexdigest()
    
    @staticmethod
    def authenticate(correo, password):
        user = UserRepository.find_by_correo(correo)
        if  user is None :
            return {"success": False, "message": "Usuario no encontrado"}
        hashed_input_password = AuthService.hash_password(password)
        if hashed_input_password == user.password_hash:
            return {"success": True, "secret_phrase": user.secret_phrase}
        return {"success": False, "message": "Contraseña incorrecta"}
       
        
    def register(correo, password, secret_phrase):
        try:
            existing_user = UserRepository.find_by_correo(correo)
            if existing_user:
                return {"success": False, "message": "Correo ya registrado"}
            password_hash = AuthService.hash_password(password)
            UserRepository.create_user(correo, password_hash, secret_phrase)
            return {"success": True, "message": "Registro exitoso"}
        except Exception as e:
            return {"success": False, "message": "Error durante el registro"}