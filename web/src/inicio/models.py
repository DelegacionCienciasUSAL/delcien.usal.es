from django.db import models

class Destacado( models.Model):
	fecha = models.DateField( blank=True, null=True, verbose_name='Fecha')
	contenido = models.CharField( max_length=150)

	def __str_( self):
		return(f"{fecha} {contenido}")
