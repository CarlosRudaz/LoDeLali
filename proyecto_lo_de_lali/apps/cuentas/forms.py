from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import cuentas_registradas, Resumen

class FormularioResumen(forms.ModelForm):
    class Meta:
        model = Resumen
        fields = [
            "cliente",
            "producto",
            "venta",
            "entrega",
            
        ]
 
        labels = {
            "cliente":"Cliente",
            "producto": "Productos",
            "venta": "Venta",
            "entrega": "Entrega",
        }
        
        widgets = {
            'fecha': forms.DateInput(attrs={'type':'date'})
        }


 
class FormularioCuentas(forms.ModelForm):
    class Meta:
        model = cuentas_registradas
        fields = [ 
            "nombre",
            "celular",
            "debe",
        ]

        labels = {
            "nombre":"Nombre y Apellido",
            "celular":"Cel",
            "debe":"Ingresa con cuenta",
        }

        
        

