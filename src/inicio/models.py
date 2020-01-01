from django.db import models
import markdownx

class Destacado( models.Model):
	fecha = models.DateField( blank=True, null=True, verbose_name='Fecha')
	contenido = models.CharField( max_length=150)

	def __str_( self):
		return(f"{fecha} {contenido}")

class PaginaInicio( models.Model):
    fotoFacultad = models.ImageField(upload_to='images/')
    bienvenida = markdownx.models.MarkdownxField()
    mantente_al_dia = markdownx.models.MarkdownxField()

    def __str_( self):
        return(f"{fecha} {contenido}")

class Seccion( models.Model):
    titulo = models.CharField( max_length=150)
    mantente_al_dia = markdownx.models.MarkdownxField()

    def __str_( self):
        return(f"{fecha} {contenido}")