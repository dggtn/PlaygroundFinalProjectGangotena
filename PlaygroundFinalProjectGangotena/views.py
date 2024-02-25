import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from PlaygroundFinalProjectGangotena.form import PostCreation, UserCreationFormCustom,UserEditForm
from modelos.models import Avatar, Post
from modelos.models import Usuarios
from modelos.models import Comentarios
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm

def posts(request):
    template = loader.get_template('posts.html')
    
    query = request.GET.get('query')
    if query is None:
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(titulo__icontains=query)

    contexto = {
        'posts': posts
    }

    html = template.render(contexto, request)
    return HttpResponse(html)

def postPorId(request,id):
  postPorId = Post.objects.get(pk=id)
  template = loader.get_template('post.html')
  context = {
    'post': postPorId,
    'comentarios': Comentarios.objects.filter(post__pk=postPorId.id),
  }
  return HttpResponse(template.render(context, request))

def nuevoPost(request):
    usuario = Usuarios.objects.get(email= request.user.email)
    template = loader.get_template('nuevoPost.html')
    form =  PostCreation(initial={'id':usuario.id, 'autor':usuario.id})
    context = {
    'usuario': usuario,
    'form':form
  }
    return HttpResponse(template.render(context, request))
   
def publicar(request):
    if request.method == 'POST':
        formulario = PostCreation(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()        
            return redirect('posts')
        else:
            return HttpResponse(formulario.errors)            

def usuarios(request):
    template = loader.get_template('usuarios.html')
    
    query = request.GET.get('query')
    if query is None:
        usuarios = Usuarios.objects.all()
    else:
        usuarios= Usuarios.objects.filter(nombre__icontains=query)

    contexto = {
        'usuarios': usuarios
    }
    html = template.render(contexto, request)
    return HttpResponse(html)


def usuarioPorId(request,id):
  usuarioPorId = Usuarios.objects.get(pk=id)
  template = loader.get_template('usuario.html')
  context = {
    'usuario': usuarioPorId,
  }
  return HttpResponse(template.render(context, request))

def nuevoUsuario(request):
    template = loader.get_template('nuevoUsuario.html')
    html = template.render(request=request)
    return HttpResponse(html)

def guardar(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        apodo = request.POST['apodo']
        pais = request.POST['pais']

        Usuarios(nombre = nombre, apellido =apellido,apodo=apodo,pais=pais).save()
    return redirect('usuarios')


def nuevoComentario(request):
    usuario = Usuarios.objects.get(email= request.user.email)
    template = loader.get_template('nuevoComentario.html')
    context = {
    'usuario': usuario,
  }
    return HttpResponse(template.render(context, request))


def comentar(request):
    if request.method == 'POST':
        autor = request.POST['autor']
        cuerpo = request.POST['cuerpo']
        post = Post(id = request.POST['id'] )
        Comentarios(autor=autor, cuerpo=cuerpo, post=post).save()
    return redirect('postPorId', id = post.id)

def index(request):
    template = loader.get_template('index.html')
    html = template.render(request=request)
    return HttpResponse(html)

def login_request(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario =  form.cleaned_data.get("username")
            contrasenia = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password = contrasenia)
            login(request,user)
            return render(request, "index.html", {"mensaje": f"Bienvenido {user.username}"})
    return render(request, "login.html", {"form":form})

def register(request):
    form = UserCreationFormCustom()
    if request.method == "POST":
        form = UserCreationFormCustom(request.POST)
        if form.is_valid():
            user = form.save()
            avatar = Avatar(usuario=user, imagen=form.cleaned_data['imagen'])
            avatar.save()
            usuario = Usuarios(nombre = form.cleaned_data['nombre'],apellido = form.cleaned_data['apellido'],apodo = form.cleaned_data['apodo'],pais = form.cleaned_data['pais'],email = form.cleaned_data['email'])
            usuario.save()
            return render(request,"index.html",{"mensaje":"Usuario Creado:)"})
            
    return render (request,"registro.html", {"form":form})

def editarPerfil(request):
    if request.method == 'GET':
     template = loader.get_template('editarPerfil.html')
     usuario= request.user
     form =  PasswordChangeForm(usuario)
     context = {
     'usuario': usuario,
     'form':form
  }
     html = template.render(context, request)
     return HttpResponse(html)
    else:
     form = PasswordChangeForm(data=request.POST, user=request.user)
     if form.is_valid():
      form.save()
      return render(request,"index.html",{"mensaje":"Perfil Actualizado)"})
        
def bio(request):
    template = loader.get_template('bio.html')
    
    query = request.GET.get('query')
    if query is None:
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(titulo__icontains=query)

    contexto = {
        'posts': posts
    }

    html = template.render(contexto, request)
    return HttpResponse(html)

    
class CambiarContrasenia(LoginRequiredMixin,PasswordChangeView):
        template_name="cambiarContrasenia.html"
        succes_url = reverse_lazy('cambiarContrasenia')
