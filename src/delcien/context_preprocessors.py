from delcien.models import Delegacion, RedSocial

def delegation_and_social_accounts(request):
    return {
        'delegacion': Delegacion.objects.first(),
        'social': RedSocial.objects.all()
    }