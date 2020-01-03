from django.db import models

class RedSocial(models.Model):
    SOCIAL_ICON_CHOICES = (
        ('fi-xnsuxl-twitter', 'Twitter'),
        ('fi-xnsuxl-instagram', 'Instagram'),
        ('fi-xnsuxl-facebook-circle', 'Facebook'),
        ('fi-xnsuxl-github', 'Github'),
        ('fi-xnsuxl-youtube', 'Youtube'),
        ('fi-xnsuxl-twitch-glitch', 'Twitch'),
    )
    social_max_length = max(map(lambda x: len(x[0]), SOCIAL_ICON_CHOICES))

    red = models.CharField( max_length=150)
    perfil = models.CharField( max_length=150)
    icono = models.CharField( max_length=social_max_length, choices=SOCIAL_ICON_CHOICES, default='fi-xnsuxl-twitter')

    class Meta:
        verbose_name = 'Redes Sociales'
        verbose_name_plural = 'Redes Sociales'

    def __str__(self):
        return(self.red)

class Delegacion(models.Model):
    facultad = models.CharField( max_length=150)
    direccion = models.CharField( max_length=150)
    telefono = models.CharField( max_length=150)
    email = models.CharField( max_length=150)

    class Meta:
        verbose_name = 'Detalles de la Delegacion'
        verbose_name_plural = 'Detalles de la Delegacion'

    def __str__( self):
        return(f"Delegacion de estudiantes ({self.facultad})")