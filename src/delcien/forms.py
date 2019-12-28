from django import forms

class ColaboradorFormulario(forms.Form):
    colaborador = forms.EmailField( max_length=100)

class PropuestaFormulario(forms.Form):
    propuesta = forms.CharField()
