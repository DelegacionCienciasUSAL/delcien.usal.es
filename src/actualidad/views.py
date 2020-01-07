from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from actualidad.models import Articulo, Evento

# Create your views here.	

def main( request, pagina=1):
	articulos_pagina = 12
	
	try:
		paginas = Paginator( Articulo.objects.all(), articulos_pagina)

		if( not pagina):
			pagina = 1
		else:
			pagina = int( pagina)

		try:
			articulos = paginas.page(pagina)
		except PageNotAnInteger:
			articulos = paginas.page(1)
		except EmptyPage:
			articulos = paginas.page(paginas.num_pages)

		return( render( request, 'actualidad/main.html', {
			'articulos' : articulos,
			'pagina': pagina, 
            'Titulo' : 'Actualidad'}))	
	except Exception as e:
		raise e

def details(request, id):
	try:
		articulo = Articulo.objects.get(pk=id)
		context = {
			'articulo': articulo,
		}

		return render(request, 'actualidad/details.html', context)
	except Exception as e:
		raise(e)
