from django import forms

class Duda(forms.Form):
	ambitos = ['Facultad de Ciencias',
		'Ing. Informática',
		'Ing. Geológica',
		'Geología',
		'Matemáticas',
		'Física',
		'Estadística']
    ambito = forms.ChoiceField(choices=ambitos)
	nombre = forms.CharField()
	correo = forms.EmailField( max_length=100)  
	duda = forms.CharField()
	extra = forms.CharField()