from django.urls import path
from perfiles import views

urlpatterns = [
  path('', views.ver_perfil, name='ver_perfil'),
  path('actualizar_foto', views.actualizar_foto_de_perfil, name='actualizar_foto'),
  path('actualizar_perfil', views.actualizar_perfil, name='actualizar_perfil'),
]