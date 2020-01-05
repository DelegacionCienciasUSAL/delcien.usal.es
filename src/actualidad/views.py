from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from actualidad.models import Noticia

# Create your views here.	

def main( request, pagina=1):
	noticias_pagina = 12
	
	try:
		paginas = Paginator( Noticia.objects.all(), noticias_pagina)

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

		return( render( request, 'actualidad/main.html', {
			'noticias' : noticias,
			'pagina': pagina, 
            'Titulo' : 'Actualidad'}))	
	except Exception as e:
		raise e

def details(request, id):
	try:
		noticia = Noticia.objects.get(pk=id)
		context = {
			'noticia': noticia,
		}

		return render(request, 'actualidad/details.html', context)
	except Exception as e:
		raise(e)
