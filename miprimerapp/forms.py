from django import forms

class FormCafe(forms.Form):
    nombre = forms.CharField(max_length=30)
    tostado = forms.CharField(max_length=30)
    cuerpo = forms.IntegerField()
    
class BuscarCafe(forms.Form):
        nombre = forms.CharField(max_length=30)

