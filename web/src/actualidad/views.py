from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from actualidad.models import Noticia

# Create your views here.	

def main( request, pagina=1):
	noticias_pagina = 2
	carreras = ( 'NON', 'INF', 'IQI', 'FIS', 'EST', 'MAT', 'GEO',)
	categorias = ( 'NON', 'EVE', 'FOR', 'ACA', 'UNI', 'CON',)
	(categoria, carrera) = ('NON', 'NON')
	
	try:
		if( ('carrera' in request.GET) and ('categoria' in request.GET)):
			categoria = request.GET['categoria']
			carrera = request.GET['carrera']
			
			if( (request.GET['carrera'] in carreras) and (request.GET['carrera'] != 'NON')):
				lista_noticias = set( Noticia.objects.filter(carrera=carrera))
			else:
				lista_noticias = set( Noticia.objects.all())

			if( (request.GET['categoria'] in categorias) and (request.GET['categoria'] != 'NON')):
				lista_noticias.intersection_update( Noticia.objects.filter(categoria=categoria))
		else:
			lista_noticias = Noticia.objects.all();

		paginas = Paginator( list( lista_noticias), noticias_pagina)

		if( not pagina):
			pagina = 1
		else:
			pagina = int( pagina)

		try:
			noticias = paginas.page(pagina)
		except PageNotAnInteger:
			noticias = paginas.page(1)
		except EmptyPage:
			noticias = paginas.page(paginas.num_pages)
#
#		if( len( noticias) >= pagina*noticias_pagina):
#			noticias = noticias[ (pagina-1)*noticias_pagina : (pagina*noticias_pagina-1)]
#		elif( len( noticias) > (pagina-1)*noticias_pagina):
#			noticias = noticias[ (pagina-1)*noticias_pagina : (len( noticias) - 1)]

		return( render( request, 'actualidad/main.html', {
			'noticias' : noticias,
			'pagina': pagina, 
			'carrera': carrera, 
			'categoria': categoria,
                        'Titulo' : 'Actualidad'}))	
	except Exception as e:
		raise e
