from django.db import models
import markdownx

class Articulo( models.Model):
	titulo = models.CharField( max_length=30)
	descripcion_corta = models.CharField( max_length=280)
	fecha = models.DateField( auto_now_add=True, verbose_name='Fecha')
	noticia = markdownx.models.MarkdownxField()

	def __str_( self):
		return( "%s : %s : %s"%( self.titulo, self.fecha))

class Evento( models.Model):
	titulo = models.CharField( max_length=30) 
	fecha = models.DateField( verbose_name='Fecha')
	descripcion = markdownx.models.MarkdownxField()
	enlace = models.CharField(blank=True, max_length=2000)

	def __str_( self):
		return( "%s : %s : %s"%( self.titulo, self.fecha))