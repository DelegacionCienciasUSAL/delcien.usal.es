from django.shortcuts import render
from django.http import Http404
from inicio.models import Destacado, Seccion, PaginaInicio
from delcien.models import Delegacion

# Create your views here.
def main( request):
    destacado = Destacado.objects.first()
    if destacado == None:
        destacado = 'Ninguna noticia destacada'
    else:
        destacado = destacado.contenido
    datos_delegacion = Delegacion.objects.first()
    contenido = PaginaInicio.objects.first()
    return( render( request, 'inicio/main.html', 
            {'titulo' : 'Inicio', 'destacado':destacado, 'delegacion': datos_delegacion, 'contenido': contenido}))
