from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponseBadRequest
from auth_app.services.auth_service import AuthService

@api_view(['POST'])
def login(request):
    correo = request.data.get('correo')
    password = request.data.get('password')
    if correo and password:
        result = AuthService.authenticate(correo, password)
        return Response(data=result, status=200 if result["success"] else 401)
    else:
        return HttpResponseBadRequest("Correo y contraseña son requeridos")
    
@api_view(['POST'])
def register(request):
    correo = request.data.get('correo')
    password = request.data.get('password')
    secret_phrase = request.data.get('secret_phrase')
    if correo and password and secret_phrase:
        result = AuthService.register(correo, password, secret_phrase)
        return Response(data=result, status=201 if result["success"] else 400)
    else:
        return HttpResponseBadRequest("Correo, contraseña y frase secreta son requeridos")