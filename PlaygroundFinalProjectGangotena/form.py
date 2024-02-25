import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User

from modelos import models

class UserCreationFormCustom(UserCreationForm):
    username = forms.CharField(label="Usuario")
    email = forms.EmailField()
    nombre = forms.CharField(label="Nombre")
    apellido =forms.CharField(label="Apellido")
    apodo = forms.CharField(label="Apodo")
    pais = forms.CharField(label="Pais")
    password1 = forms.CharField(label="contrasena:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="repetir contrasena", widget=forms.PasswordInput)
    imagen = forms.ImageField(label="Avatar",required=False)
    class Meta:
        model = User
        fields =  ['username','email','password1','password2', 'imagen']       
        help_texts = {k:"" for k in fields}

class UserEditForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['password']

class PostCreation(forms.ModelForm):
    titulo = forms.CharField(label="Titulo")
    autor = forms.ModelChoiceField(queryset=models.Usuarios.objects.all(), widget=forms.HiddenInput())
    imagen = forms.ImageField(label="Imagen",required=False)
    cuerpo = forms.CharField(label="Cuerpo")
    fecha = forms.DateTimeField(widget=forms.HiddenInput())
    class Meta:
        model = models.Post
        fields =  ['titulo','imagen','cuerpo', 'autor', 'fecha']       
        help_texts = {k:"" for k in fields}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha'].initial = datetime.datetime.now()
