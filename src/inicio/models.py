from django.db import models
import markdownx

class Alerta( models.Model):
    contenido = models.CharField( max_length=150)

    class Meta:
        verbose_name = 'Alerta'
        verbose_name_plural = 'Alertas'

    def __str_( self):
        return(f"Alerta")

class PaginaInicio( models.Model):
    fotoFacultad = models.ImageField(blank=True, null=True, upload_to='images/')
    bienvenida = markdownx.models.MarkdownxField()
    mantente_al_dia = markdownx.models.MarkdownxField()

    class Meta:
        verbose_name = 'Contenido de la página de inicio'
        verbose_name_plural = 'Contenido de la página de inicio'

    def __str_( self):
        return(f"Página de inicio")

class Seccion( models.Model):
    titulo = models.CharField(max_length=150)
    contenido = markdownx.models.MarkdownxField()

    class Meta:
        verbose_name = 'Secciones extra'
        verbose_name_plural = 'Secciones extra'

    def __str_( self):
        return(self.titulo)