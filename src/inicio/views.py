from django.shortcuts import render
from django.http import Http404
from inicio.models import Alerta, Seccion, PaginaInicio
from delcien.models import Delegacion

# Create your views here.
def main( request):
    alertas = Alerta.objects.all()
    datos_delegacion = Delegacion.objects.first()
    contenido = PaginaInicio.objects.first()
    secciones = Seccion.objects.all()

    context = {
        'titulo' : 'Inicio', 
        'alertas': alertas, 
        'delegacion': datos_delegacion, 
        'contenido': contenido,
        'sections': secciones
        }
    return( render( request, 'inicio/main.html', context))
