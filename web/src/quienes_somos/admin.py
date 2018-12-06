from django.contrib import admin
from quienes_somos.models import Presidente, Secretario, Tesorero, Vocal
from quienes_somos.models import Vocalia
from quienes_somos.models import Vicepresidente, Vicesecretario, Vicetesorero
from quienes_somos.models import Colaborador

admin.site.register( Presidente)
admin.site.register( Vicepresidente)
admin.site.register( Vicesecretario)
admin.site.register( Vicetesorero)
admin.site.register( Secretario)
admin.site.register( Tesorero)
admin.site.register( Vocal)
admin.site.register( Vocalia)
admin.site.register( Colaborador)
