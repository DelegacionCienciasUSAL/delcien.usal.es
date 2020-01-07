from django.shortcuts import render
from django.http import Http404
from inicio.models import Alerta, Seccion, PaginaInicio
from delcien.models import Delegacion
from actualidad.models import Articulo, Evento

# Create your views here.
def main( request):
    alertas = Alerta.objects.all()
    datos_delegacion = Delegacion.objects.first()
    contenido = PaginaInicio.objects.first()
    secciones = Seccion.objects.all()

    articulos = Articulo.objects.order_by('-id')[:3]
    eventos = Evento.objects.order_by('fecha')[:3]

    context = {
        'titulo' : 'Inicio', 
        'alertas': alertas, 
        'delegacion': datos_delegacion, 
        'contenido': contenido,
        'sections': secciones,
        'articulos': articulos,
        'eventos': eventos,
    }
    return( render( request, 'inicio/main.html', context))
