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
from PlaygroundFinalProjectGangotena.views import CambiarContrasenia ,editarPerfil,index,posts,postPorId,nuevoPost,publicar,usuarios,usuarioPorId,register,guardar,comentar,nuevoUsuario,nuevoComentario,login_request,bio
from django.contrib.auth.views import LogoutView
from modelos import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', index, name="index"),
    path('bio', bio, name="bio"),
    path('posts/', posts, name="posts"),
    path('posts/postPorId/<int:id>', postPorId, name="postPorId"),
    path('posts/nuevo', nuevoPost, name='nuevoPost'),
    path('admin/', admin.site.urls),
    path('posts/publicar/', publicar, name="publicar"),
    path('usuarios/', usuarios, name="usuarios"),
    path('usuarios/usuarioPorId/<int:id>', usuarioPorId, name="usuarioPorId"),
    path('usuarios/nuevo/', nuevoUsuario, name="nuevoUsuario"),
    path('usuarios/nuevo/guardar/', guardar, name="guardar"),
    path('comentarios/comentar/', comentar, name="comentar"),
    path('login',login_request,name="login"),
    path('registro',register,name="registro"),
    path('logout',LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('editarPerfil/',editarPerfil, name="editarPerfil"),
    path('editarPerfil/actualizarPerfil/',editarPerfil, name="actualizarPerfil"),
    path('cambiarContrasenia',CambiarContrasenia.as_view(template_name="cambiarContrasenia.html"), name="cambiarContrasenia"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)