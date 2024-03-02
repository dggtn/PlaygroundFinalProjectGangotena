from django import forms
from perfiles import models

class ActualizarFotoDePerfil(forms.ModelForm):
  class Meta:
    model = models.Perfil
    fields = ("avatar",)

class ActualizarPerfil(forms.ModelForm):
  class Meta:
    model = models.Perfil
    fields = ("apodo", "pais")
