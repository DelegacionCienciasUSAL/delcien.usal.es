from delcien.models import Delegacion, RedSocial
from delcien.urls import URL_TO_NAME

def delegation_and_social_accounts(request):
    base_path = 'inicio' if request.path == '/' else request.path.split('/')[1]
    app_name = URL_TO_NAME[base_path]

    return {
        'delegacion': Delegacion.objects.first(),
        'social': RedSocial.objects.all(),
        'base_path': base_path,
        'app_name': app_name,
    }