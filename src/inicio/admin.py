from markdownx.admin import MarkdownxModelAdmin
from django.contrib import admin
import inicio

class PaginaInicioAdmin(MarkdownxModelAdmin):
    def has_add_permission(self, *args, **kwargs):
        return not inicio.models.PaginaInicio.objects.exists()

admin.site.register(inicio.models.Alerta)
admin.site.register(inicio.models.PaginaInicio, PaginaInicioAdmin)
admin.site.register(inicio.models.Seccion, MarkdownxModelAdmin)