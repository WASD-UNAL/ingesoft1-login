from auth_app.domain.models import Ingesoft1User
def find_by_correo(correo):
    Ingesoft1User.objects.get(correo=correo)

def create_user(correo, password_hash, secret_phrase):
    user = Ingesoft1User(correo=correo, password_hash=password_hash, secret_phrase=secret_phrase)
    user.save()
    return user