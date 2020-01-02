from django.db import models

class Recurso( models.Model):
	CONSTRUCCION = 'CN'
	VALIDO = 'VA'
	INACCESIBLE = 'IN'
	DESACTUALIZADO = 'DS'
	OPCIONES_VALIDEZ = (
		( CONSTRUCCION, 'Construcción'),
		( VALIDO, 'Válido'),
		( INACCESIBLE, 'Inaccesible'),
		( DESACTUALIZADO, 'Desactualizado'),
	)

	PDF = 'PF'
	POWERPOINT = 'PT'
	WORD = 'WD'
	EXCEL = 'XL'
	HTML = 'HT'
	ZIP = 'ZP'
	OPCIONES_FICHERO = (
		(PDF, 'Pdf'),
		(POWERPOINT, 'Powerpoint'),
		(WORD, 'Word'),
		(EXCEL, 'Excel'),
		(HTML, 'Html'),
		(ZIP, 'Zip'),
	)	

	DELEGACION = 'DL'
	UNIVERSIDAD = 'UN'
	ESTUDIANTE = 'ES'
	REPRESENTANTE = 'RE'
	OPCIONES_CATEGORIA = (
		(DELEGACION, 'Delegación'),
		(UNIVERSIDAD, 'Universidad'),
		(ESTUDIANTE, 'Estudiantes'),
		(REPRESENTANTE, 'Representantes'),
	)	

	nombre = models.CharField( max_length=30)
	fecha_edicion = models.DateField( )
	tipo_fichero = models.CharField( max_length=2, choices=OPCIONES_FICHERO)
	validez = models.CharField( max_length=2, choices=OPCIONES_VALIDEZ)
	categoria = models.CharField( max_length=2, choices=OPCIONES_CATEGORIA)
	descripcion = models.CharField( max_length=90)
	fichero = models.URLField()

	def __str__( self):
		return( "%s : %s %s"%( self.nombre, self.tipo_fichero, self.validez))