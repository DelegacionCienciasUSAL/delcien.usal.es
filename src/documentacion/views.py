from django.shortcuts import render
from django.http import Http404
from documentacion.models import Recurso

# Create your views here.
def main( request):
	RecursosEstudiante = Recurso.objects.filter(categoria='ES')
	RecursosRepresentacion = Recurso.objects.filter(categoria='RE')
	RecursosDelegacion = Recurso.objects.filter(categoria='DL')
	RecursosUniversidad = Recurso.objects.filter(categoria='UN')

	return( render( request, 'documentacion/main.html', {
		'doc_estudiante': RecursosEstudiante, 
		'doc_representante': RecursosRepresentacion, 
		'doc_delegacion': RecursosDelegacion, 
		'doc_universidad': RecursosUniversidad, 
                'Titulo' : 'Documentación'}))