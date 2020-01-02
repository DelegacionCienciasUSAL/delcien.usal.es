from django.contrib import admin
from actualidad.models import Noticia

class NoticiaAdmin( admin.ModelAdmin):
	list_filter = ( 'categoria',)

admin.site.register( Noticia, NoticiaAdmin)