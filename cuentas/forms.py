from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pkg_resources import require


class MyUserCreationForm(UserCreationForm):
    
    username = forms.CharField(label="Username", max_length=30)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Password",widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username","password1", "password2"]
        help_text = { key:"" for key in fields}



class MyUserEditForm(forms.Form):
    first_name = forms.CharField(label="Nombre", max_length=30,required=False)
    last_name = forms.CharField(label="Apellido", max_length=30,required=False)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput,required=False)
    password2 = forms.CharField(label="Repetir Password",widget=forms.PasswordInput,required=False)
    avatar = forms.ImageField(required=False)
    
    