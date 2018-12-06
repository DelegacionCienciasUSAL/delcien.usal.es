from django.shortcuts import render
from django.http import Http404

# Create your views here.
def main( request):
    return( render( request, 'estructura_interna/main.html', {'Titulo'
        : 'Estructura Interna'}))
