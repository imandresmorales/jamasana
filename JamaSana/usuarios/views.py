
from rest_framework import viewsets, permissions
from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login

from .models import Cliente
from .models import Administrador
from .models import Vendedor

from .serializers import ClienteSerializer
from .serializers import AdministradorSerializer
from .serializers import VendedorSerializer
# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ClienteSerializer

class AdministradorViewSet(viewsets.ModelViewSet):
    queryset = Administrador.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AdministradorSerializer


class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = VendedorSerializer


def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "usuarios/welcome.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

def register(request):
    return render(request, "users/register.html")

def login(request):
     # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                #do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})

def logout(request):
    
    # Finalizamos la sesión
    #do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
