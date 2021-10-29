from django.db import models
from django.db.models.fields.related import ForeignKey


# Create your models here.

#MODELO PARA MANEJAR EL REGISTRO DE CLIENTES
class cuentas_registradas (models.Model):
    id_cliente = models.AutoField(primary_key=True, auto_created=True)
    nombre = models.CharField("Nombre Cliente", max_length=30, blank=False, null=False, unique=True)
    debe = models.BooleanField("Tiene Saldo/ No tiene", default=False)
    total = models.FloatField("total", null=True, default=0)
    fecha = models.DateField(auto_now_add=True)
    celular = models.CharField("Celular", blank=False, unique=True, null=False, max_length=10)

    def __str__(self):
        x = f"{self.nombre} -------> cel: {self.celular}"
        return x
    
     
#MODELO PARA MANEJAR EL MOVIMIENTO DE CUENTAS DE CADA CLIENTE
class Resumen(models.Model):
    cliente = models.ForeignKey(cuentas_registradas, on_delete=models.CASCADE)
    fecha = models.DateField("fecha", auto_now_add=True)
    producto = models.CharField("producto", max_length=200)
    venta = models.FloatField("venta", default=0)
    entrega = models.FloatField("entrega", blank=True, null=True, default=0)
    saldo = models.FloatField("saldo", blank=True, null=True)
    total = models.FloatField("total", null=True, default=0)
    
    
    
    

    
    
    
    
    def __str__(self):
        x = "Cuenta de " + self.cliente.nombre
        return x

    



