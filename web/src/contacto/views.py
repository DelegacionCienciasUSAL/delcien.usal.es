from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseRedirect

# Create your views here.
def main( request):
	return( render( request, 'contacto/main.html', {'Titulo' : 'Contacto'}))

def get_duda(request):
    referer = request.META.get('HTTP_REFERER')
    if request.method == 'GET':
        nombre = request.GET.get('nombre')
        correo = request.GET.get('correo')
        ambito  = request.GET.get('ambito')
        duda = request.GET.get('duda')
        extra = request.GET.get('extra')
        prev_url = request.GET.get('prev_url')
        if(nombre != None and duda != None and prev_url != None):
            subject = f"WEBPAGE : Duda de {nombre} sobre {ambito}"
            message = f"{nombre} ( {correo} ):\n"
            message = message + f"Ambito : {ambito}\nDuda : \n{duda}\n\n{extra}"
            from_email = settings.EMAIL_HOST_USER
            to_list = [settings.EMAIL_HOST_USER,]
            send_mail(subject, message, from_email, to_list)

    return HttpResponseRedirect(referer)

def get_colab(request):
    referer = request.META.get('HTTP_REFERER')
    if request.method == 'GET':
        nombre = request.GET.get('nombre')
        correo = request.GET.get('correo')
        ambito  = request.GET.get('ambito')
        idea = request.GET.get('idea')
        extra = request.GET.get('extra')
        prev_url = request.GET.get('prev_url')
        if(nombre != None and idea != None and prev_url != None):
            subject = f"WEBPAGE : Propuesta de colaboración de {nombre} sobre {ambito}"
            message = f"{nombre} ( {correo} ):\n"
            message = message + f"Ambito : {ambito}\nidea : \n{idea}\n\n{extra}"
            from_email = settings.EMAIL_HOST_USER
            to_list = [settings.EMAIL_HOST_USER,]
            print(f'colab subject : {subject}\n{from_email}\ncorreo : \n{message}')
            send_mail(subject, message, from_email, to_list)

    return HttpResponseRedirect(referer)