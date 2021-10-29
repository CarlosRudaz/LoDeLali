from django.core.exceptions import ObjectDoesNotExist
from .forms import FormularioCuentas, FormularioResumen
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import cuentas_registradas, Resumen
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    #cuentas = FormularioCuentas()
    return render(request, 'index.html')


class Cuentas():
    # CARGAMOS LOS DATOS PARA EL REGISTRO DE UN NUEVO CLIENTE A LA BASE DE DATOS.
    @login_required
    def cargar_cuentas(request):
        
        if request.method == "POST":
            
            cuentas = FormularioCuentas(request.POST)

            mensaje = False
            if cuentas.is_valid():
                cuentas.save()
                

                if cuentas.save():
                    cuentas = FormularioCuentas()
                    messages.success(request, "¡Cuenta registrada con éxito!")
                    return redirect("lista_clientes")
                
            return render(request, 'cuentas/cargar_cuentas.html', {"form": cuentas, 'mensaje':mensaje})
        else: 
            cuentas = FormularioCuentas()
        return render(request, 'cuentas/cargar_cuentas.html', {"form": cuentas})



    # AGREGAMOS UN NUEVO MOVIMIENTO EN LA CUENTA DE ALGÚN CLIENTE YA REGISTRADO.
    @login_required
    def cargar_resumen(request, id_cliente):
        
        cliente = cuentas_registradas.objects.get(id_cliente = id_cliente)
        error = False
 
        if request.method == "POST":
            nuevo_resumen = FormularioResumen(request.POST)
            if nuevo_resumen.is_valid():
                nuevo_resumen.save()
                
                nuevo_resumen = Resumen.objects.filter(producto=request.POST["producto"]).last()
                total = cliente.total
                
                if total == None:
                    total = 0 

                venta = float(nuevo_resumen.venta)
                entrega = float(nuevo_resumen.entrega)
                
                if entrega == 0:
                    total += venta
                    
                    cliente.total = nuevo_resumen.total = nuevo_resumen.saldo = total
                else:
                    total += venta
                    saldo = total - entrega

                    nuevo_resumen.total = total
                    cliente.total = nuevo_resumen.saldo = saldo

                if cliente.total <= 0:
                    cliente.debe = False
                else:
                    cliente.debe = True

                cliente.save()

                nuevo_resumen.save()

                nuevo_resumen = FormularioResumen()


                return redirect("../lista_clientes")
            else:
                error = True

        nuevo_resumen = FormularioResumen()
        
        ctx={
            "form":nuevo_resumen,
            "cliente":cliente,
            "error":error,
        }
        return render(request, "cuentas/cargar_resumen.html", ctx)        


    # AGREGAMOS EL LINK EN EL NOMBRE DE CADA CLIENTE PARA QUE SE PUEDA ACCEDER A SU PLANILLA DE COMPRAS
    @login_required
    def ver_resumen(request, id_cliente):
        cliente = cuentas_registradas.objects.get(id_cliente = id_cliente)
        datos = Resumen.objects.filter(cliente = cliente)
        
        paginador = Paginator(datos, 5)
        pagina_actual = request.GET.get("page")
        datos = paginador.get_page(pagina_actual)


        ctx = {
            "cliente":cliente,
            "datos": datos #.order_by("fecha"),
        }

        return render(request, "cuentas/ver_resumen_cliente.html", ctx)


    # LISTA DE CLIENTES REGISTRADOS QUE TIENEN O NO DEUDA.
    @login_required
    def listar(request):
        buscar = request.GET.get("buscar")
        if buscar:
            cuentas = cuentas_registradas.objects.filter(nombre__icontains = buscar, debe = True)
            cuentas2 = cuentas_registradas.objects.filter(nombre__icontains = buscar, debe = False)
            # cuentas = cuentas_registradas.objects.filter(Q(nombre=buscar) | Q(apellido=buscar)).distinct()
        else:
            cuentas = cuentas_registradas.objects.filter(debe = True)
            cuentas2 = cuentas_registradas.objects.filter(debe = False)

        ctx = { 
            "cuentas": cuentas.order_by("nombre"),
            "cuentas2": cuentas2.order_by("nombre"),
        }
        
        return render(request, 'cuentas/lista_clientes.html', ctx)

    # ELIMINAR CUENTA
    def eliminar_cuenta(request, id_cliente):
        cuenta = cuentas_registradas.objects.get(id_cliente = id_cliente)
        cuenta.delete()
        return redirect('lista_clientes')


