from .forms import RegistroForm
from .models import Equipo
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.shortcuts import render



#----------------------------------- CREAMOS USUARIOS (NO STAFF) -------------------------------------------------
class Registrarse (CreateView):
    models = User
    form_class = RegistroForm
    success_url = reverse_lazy('home')
    template_name = 'registration/registrarse.html'