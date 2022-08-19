from django import forms
from ckeditor.fields import RichTextFormField


class FormCafe(forms.Form):
    nombre = forms.CharField(max_length=30)
    tostado = forms.CharField(max_length=30)
    cuerpo = forms.IntegerField()
    descripcion = RichTextFormField()
    
class BuscarCafe(forms.Form):
        nombre = forms.CharField(max_length=30)

