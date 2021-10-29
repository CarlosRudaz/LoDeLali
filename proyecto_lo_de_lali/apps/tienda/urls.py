
from .views import tienda
from django.urls import path


urlpatterns = [
    path("todos/", tienda, name="todos"),
]