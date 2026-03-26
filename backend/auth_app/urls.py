from django.urls import path
from auth_app.controllers.auth_controller import login, register


urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]