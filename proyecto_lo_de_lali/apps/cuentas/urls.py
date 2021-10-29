from django.urls import path
from .views import Cuentas, index

urlpatterns = [
    path('home/', index, name='inicio'),
    path('cargar_cuentas/', Cuentas.cargar_cuentas, name='cargar_cuentas' ),
    path('lista_clientes/', Cuentas.listar, name='lista_clientes'),
    path('resumen_cliente/<int:id_cliente>', Cuentas.cargar_resumen, name="cargar_resumen"),
    path('ver_resumen/<int:id_cliente>', Cuentas.ver_resumen, name="ver_resumen"),
    path('eliminar_cuenta/<int:id_cliente>', Cuentas.eliminar_cuenta, name="eliminar_cuenta"),
]
