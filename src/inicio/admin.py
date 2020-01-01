from markdownx.admin import MarkdownxModelAdmin
from django.contrib import admin
import inicio

class PaginaInicioAdmin(admin.ModelAdmin):
    def has_add_permission(self, *args, **kwargs):
        return not inicio.models.PaginaInicio.objects.exists()

admin.site.register(inicio.models.Destacado)
admin.site.register(inicio.models.PaginaInicio, MarkdownxModelAdmin)
admin.site.register(inicio.models.Seccion, MarkdownxModelAdmin)