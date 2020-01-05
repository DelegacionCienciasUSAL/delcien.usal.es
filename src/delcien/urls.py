"""delcien URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from delcien.views import soporte, legal, get_colab, get_sug
from inicio.views import main as index

admin.site.site_header = "Portal Admin - Delegación"
admin.site.site_title = "Portal Admin de la Delegación"
admin.site.index_title = "Portal Administrativo de la Página Web de la Delegación"

URL_TO_NAME = {
    'soporte': 'Soporte',
    'legal': 'Política de Privacidad',
    'inicio': 'Inicio',
    'quienes-somos': '¿Quiénes somos?',
    'estructura-interna': 'Estructura interna de la Facultad',
    'actualidad': 'Actualidad',
    'documentacion': 'Documentacion',
    'contacto': 'Contacto',
}

urlpatterns = [
	url(r'^colaborar/$', get_colab, name='colaborar'),
    url(r'^sugerir/$', get_sug, name='sugerir'),
    url(r'^soporte/$', soporte),
    url(r'^legal/$', legal),
    url(r'^admin/', admin.site.urls),
    url(r'^inicio/', include( 'inicio.urls')),
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^quienes-somos/', include( 'quienes_somos.urls')),
    url(r'^estructura-interna/', include( 'estructura_interna.urls')),
    url(r'^actualidad/', include( 'actualidad.urls')),
    url(r'^documentacion/', include( 'documentacion.urls')),
    url(r'^contacto/', include( 'contacto.urls')),
    url(r'^$', index),
]

if settings.DEBUG == True:
    urlpatterns += [
        url(r'^uploads/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]