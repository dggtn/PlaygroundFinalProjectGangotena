from django import forms
from django.contrib.auth.forms import UserCreationForm,UserModel

class UserCreationFormCustom(UserCreationForm):
    user = forms.CharField(label="Usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label="contrasena:", widget=forms.PasswordInput)
    password2 = forms.CharField(label="repetir contrasena", widget=forms.PasswordInput)
    class Meta:
        model = UserModel
        fields =  ['user','email','password1','password2']       
        help_texts = {k:"" for k in fields}