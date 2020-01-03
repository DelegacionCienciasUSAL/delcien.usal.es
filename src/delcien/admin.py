from django.contrib import admin
from .models import Delegacion, RedSocial

class DelegacionAdmin(admin.ModelAdmin):
    def has_add_permission(self, *args, **kwargs):
        return not Delegacion.objects.exists()
        
admin.site.register(Delegacion, DelegacionAdmin)
admin.site.register(RedSocial)