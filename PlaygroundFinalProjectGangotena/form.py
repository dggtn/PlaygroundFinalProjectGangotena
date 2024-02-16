from django import forms
from django.contrib.auth.forms import UserCreationForm,UserModel

class UserCreationFormCustom(UserCreationForm):
    username = forms.CharField(label="Usuario")
    email = forms.EmailField()
    nombre = forms.CharField(label="Nombre")
    apellido =forms.CharField(label="Apellido")
    apodo = forms.CharField(label="Apodo")
    pais = forms.CharField(label="Pais")
    password1 = forms.CharField(label="contrasena:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="repetir contrasena", widget=forms.PasswordInput)
    class Meta:
        model = UserModel
        fields =  ['username','email','password1','password2']       
        help_texts = {k:"" for k in fields}
