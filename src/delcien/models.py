from django.db import models

class Delegacion(models.Model):
    facultad = models.CharField( max_length=150)
    twitter = models.CharField( max_length=150)
    github = models.CharField( max_length=150)
    instagram = models.CharField( max_length=150)
    youtube = models.CharField( max_length=150)
    twitch = models.CharField( max_length=150)
    facebook = models.CharField( max_length=150)
    direccion = models.CharField( max_length=150)
    telefono = models.CharField( max_length=150)
    email = models.CharField( max_length=150)

    def __str_( self):
        return(f"Delegacion de estudiantes ({self.facultad})")