from django.urls import path
from .views import Registrarse

urlpatterns = [
    path('signup/',Registrarse.as_view() , name='registrarse'),
]

 