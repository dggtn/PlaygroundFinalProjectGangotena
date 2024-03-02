from django.shortcuts import redirect, render
from django.contrib import messages
from perfiles import forms
from perfiles import models

# Create your views here.
def ver_perfil(request):
  context = { 'actualizarFotoDePerfilForm': forms.ActualizarFotoDePerfil()}
  perfil, creado = models.Perfil.objects.get_or_create(usuario=request.user)
  context['actualizarPerfil'] = forms.ActualizarPerfil(instance=perfil)

  return render(request,"perfiles/index.html", context)

def actualizar_foto_de_perfil(request):
  if request.method == 'POST':
    form = forms.ActualizarFotoDePerfil(request.POST, request.FILES, instance=request.user.perfil)

    if form.is_valid():
      form.save()
      messages.success(request, 'Foto actualizada con éxito')
  return redirect('ver_perfil')

def actualizar_perfil(request):
  if request.method == 'POST':
    form = forms.ActualizarPerfil(request.POST, instance=request.user.perfil)
    if form.is_valid():
      form.save()
      messages.success(request, 'Perfil actualizado con éxito')
  return redirect('ver_perfil')