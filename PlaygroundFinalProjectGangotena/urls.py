"""
URL configuration for PlaygroundFinalProjectGangotena project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PlaygroundFinalProjectGangotena.views import posts, nuevoPost,publicar,usuarios,comentarios,guardar,comentar,nuevoUsuario,nuevoComentario


urlpatterns = [
    path('posts/', posts, name="posts"),
    path('posts/nuevo', nuevoPost, name='nuevoPost'),
    path('admin/', admin.site.urls),
    path('posts/publicar/', publicar, name="publicar"),
    path('usuarios/', usuarios, name="usuarios"),
    path('comentarios/', comentarios, name="comentarios"),
    path('usuarios/nuevo/', nuevoUsuario, name="nuevoUsuario"),
    path('usuarios/nuevo/guardar/', guardar, name="guardar"),
    path('comentarios/nuevo/', nuevoComentario, name="nuevoComentario"),
    path('comentarios/comentar/', comentar, name="comentar"),
    

]
