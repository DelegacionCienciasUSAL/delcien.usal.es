from django.db import models

class Noticia( models.Model):
	INGINFORMATICA = 'INF'
	INGQUIMICA = 'IQI'
	FISICA = 'FIS'
	ESTADISTICA = 'EST'
	MATEMATICAS = 'MAT'
	GEOLOGIA = 'GEO'
	OPCIONES_CARRERA = (
		( INGINFORMATICA, 'Ingeniería Informática'), 
		( INGQUIMICA, 'Ingeniería Química'), 
		( FISICA, 'Física'), 
		( ESTADISTICA, 'Estadística'), 
		( MATEMATICAS, 'Matemáticas'), 
		( GEOLOGIA, 'Geología'),	 
	)

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
	carrera = models.CharField( max_length=3, choices=OPCIONES_CARRERA)
	categoria = models.CharField( max_length=3, choices=OPCIONES_CATEGORIA)
	fecha = models.DateField( blank=True, null=True, verbose_name='Fecha')
	lugar = models.CharField( max_length=40, blank=True)
	referencia = models.URLField( blank=True)
	noticia = models.CharField( max_length=150)

	def __str_( self):
		return( "%s : %s %s : %s"%( self.titulo, self.carrera, self.categoria, self.fecha))