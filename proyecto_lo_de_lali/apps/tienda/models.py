from django.db import models

# Create your models here.

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True, auto_created=True)
    nombre = models.CharField(max_length=80)
    categoria = models.CharField(max_length=60)
    precio = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
