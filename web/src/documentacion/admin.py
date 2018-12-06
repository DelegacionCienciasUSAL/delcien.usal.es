from django.contrib import admin
from documentacion.models import Recurso

class RecursoAdmin( admin.ModelAdmin):
	list_display = ( 'nombre', 'categoria', 'fecha_edicion', 'tipo_fichero', 'validez', 'descripcion', 'fichero',)
	list_filter = ( 'categoria',)
	date_hierarchy = 'fecha_edicion'
	ordering = ( '-fecha_edicion',)

admin.site.register( Recurso, RecursoAdmin)