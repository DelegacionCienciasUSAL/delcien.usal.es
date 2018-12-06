from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseRedirect

from .forms import ColaboradorFormulario

# Create your views here.
def soporte( request):
    return( render( request, 'delcien/soporte.html'))

def get_colab(request):
    referer = request.META.get('HTTP_REFERER')
    if request.method == 'GET':
        colaborador = request.GET.get('correo-colaborador')
        prev_url = request.GET.get('prev_url')
        if(colaborador != None and prev_url != None):
            subject = "WEBPAGE : Nuevo colaborador"
            message = "Correo del nuevo colaborador : " + colaborador
            from_email = settings.EMAIL_HOST_USER
            to_list = [settings.EMAIL_HOST_USER,]
            send_mail(subject, message, from_email, to_list)

    return HttpResponseRedirect(referer)

def get_sug(request):
    referer = request.META.get('HTTP_REFERER')
    if request.method == 'GET':
        sugerencia = request.GET.get('sugerencia')
        prev_url = request.GET.get('prev_url')
        if(sugerencia != None and sugerencia != None):
            subject = "WEBPAGE : Nueva sugerencia"
            message = sugerencia
            from_email = settings.EMAIL_HOST_USER
            to_list = [settings.EMAIL_HOST_USER,]
            send_mail(subject, message, from_email, to_list)

    return HttpResponseRedirect(referer)
