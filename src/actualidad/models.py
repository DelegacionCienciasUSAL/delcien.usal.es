from django.db import models
import markdownx

class Noticia( models.Model):
	EVENTOS = 'EVE'
	FORMACION = 'FOR'
	ACADEMICA = 'ACA'
	UNIVERSIDAD = 'UNI'
	CONCURSOS = 'CON'
	OPCIONES_CATEGORIA = (
		( EVENTOS, 'Evento'),
		( FORMACION, 'Formación'),
		( ACADEMICA, 'Información Académica'),
		( UNIVERSIDAD, 'Universidad'),
		( CONCURSOS, 'Concursos'),
	)

	titulo = models.CharField( max_length=30) 
	categoria = models.CharField( max_length=3, choices=OPCIONES_CATEGORIA)
	fecha = models.DateField( auto_now_add=True, verbose_name='Fecha')
	noticia = markdownx.models.MarkdownxField()

	def __str_( self):
		return( "%s : %s : %s"%( self.titulo, self.categoria, self.fecha))