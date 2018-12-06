from django.db import models

class Cargo( models.Model):
    nombre = models.CharField( max_length=20)
    apellidos = models.CharField( max_length=40)
    imagen = models.ImageField(upload_to = 'cargos/', default = 'cargos/no_img.png')

class Presidente( Cargo):
    pass

class Secretario( Cargo):
    pass

class Tesorero( Cargo):
    pass

class Vocal( Cargo):
    pass

class Vocalia( Cargo):
    tipoVocalia = models.CharField( max_length=40)

class Vicepresidente( Cargo):
    pass

class Vicesecretario( Cargo):
    pass

class Vicetesorero( Cargo):
    pass

class Colaborador( models.Model):
    nombre = models.CharField( max_length=20)
    descripcion = models.CharField( max_length=240)
    correo = models.EmailField(max_length=70,blank=True)
    web = models.URLField(blank=True)
    logo = models.ImageField(upload_to = 'organizaciones/', default = 'organizaciones/no_img.png')
