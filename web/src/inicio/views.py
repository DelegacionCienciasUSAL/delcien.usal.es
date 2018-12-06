from django.shortcuts import render
from django.http import Http404

# Create your views here.
def main( request):
    return( render( request, 'inicio/main.html', {'Titulo' : 'Inicio'}))
