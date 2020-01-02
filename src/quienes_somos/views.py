from django.shortcuts import render
from django.http import Http404
from quienes_somos.models import *

# Create your views here.
def main( request):
	return( render( request, 'quienes_somos/main.html', {
            'Presidente': Presidente.objects.first(),
            'Secretario': Secretario.objects.first(),
            'Tesorero': Tesorero.objects.first(),
            'Vicepresidente': Vicepresidente.objects.first(),
            'Vicesecretario': Vicesecretario.objects.first(),
            'Vicetesorero' : Vicetesorero.objects.first(),
            'Vocal': Vocal.objects.first(),
            'Vocalias' : Vocalia.objects.all(),
            'Titulo' : 'Quienes Somos',
            'Colaboradores' : Colaborador.objects.all(),
            }))
