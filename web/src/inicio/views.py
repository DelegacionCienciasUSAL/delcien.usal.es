from django.shortcuts import render
from django.http import Http404
from inicio.models import Destacado

# Create your views here.
def main( request):
    destacado = Destacado.objects.first()
    if destacado == None:
        destacado = 'Ninguna noticia destacada'
    else:
        destacado = destacado.contenido
    return( render( request, 'inicio/main.html', 
            {'Titulo' : 'Inicio', 'Destacado':destacado}))
