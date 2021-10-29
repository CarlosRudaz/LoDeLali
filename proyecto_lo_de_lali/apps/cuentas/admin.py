from django.contrib import admin
from .models import cuentas_registradas, Resumen
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class cuentas_registradasResource(resources.ModelResource):
    class Meta:
        model = cuentas_registradas



class ResumenResource(resources.ModelResource):
    class Meta:
        model = Resumen


class cuentas_registradasAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre', "debe", "celular",) #ES PARA LOS TÍTULOS DEL ADMIN
    search_fields = ('nombre',) #CREA UN BUSCADOR QUE SE BASA EN LOS PARÁMETROS QUE LE PASEMOS
    ordering = ["nombre"] #ORDENA LOS REGISTROS
    resource_class = cuentas_registradasResource #APP EXTERNA PARA IMPORTAR DATOS REGISTRADOS
    

class ResumenAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    autocomplete_fields = ['cliente']
    ordering = ["cliente"]
    resource_class = ResumenResource 




admin.site.register(cuentas_registradas, cuentas_registradasAdmin)
admin.site.register(Resumen, ResumenAdmin)
