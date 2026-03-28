from auth_app.domain.models import Ingesoft1User
from django.core.exceptions import ObjectDoesNotExist

def find_by_correo(correo):
    try:
        # Agregamos el return y capturamos el error si no existe
        return Ingesoft1User.objects.get(correo=correo)
    except ObjectDoesNotExist:
        return None

def create_user(correo, password_hash, secret_phrase):
    user = Ingesoft1User(correo=correo, password_hash=password_hash, secret_phrase=secret_phrase)
    user.save()
    return user