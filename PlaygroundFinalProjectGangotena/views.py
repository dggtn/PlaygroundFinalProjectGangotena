from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from PlaygroundFinalProjectGangotena.form import UserCreationFormCustom
from modelos.models import Post
from modelos.models import Usuarios
from modelos.models import Comentarios
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate

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
  }
  return HttpResponse(template.render(context, request))

def nuevoPost(request):
    template = loader.get_template('nuevoPost.html')
    html = template.render(request=request)
    return HttpResponse(html)
   
def publicar(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        cuerpo = request.POST['cuerpo']
        Post(titulo=titulo, cuerpo=cuerpo).save()
    return redirect('posts')

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

def comentarios(request):
    template = loader.get_template('comentarios.html')
    
    comentarios = Comentarios.objects.all()
    contexto = {
        'comentarios': comentarios
    }

    html = template.render(contexto, request)
    return HttpResponse(html)



def nuevoComentario(request):
    template = loader.get_template('nuevoComentario.html')
    html = template.render(request=request)
    return HttpResponse(html)

def comentar(request):
    if request.method == 'POST':
        autor = request.POST['autor']
        cuerpo = request.POST['cuerpo']
        Comentarios(autor=autor, cuerpo=cuerpo).save()
    return redirect('comentarios')

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
            return render(request, "/index.html", {"mensaje": f"Bienvenido {user.username}"})
    return render(request, "login.html", {"form":form})

def register(request):
    form = UserCreationFormCustom()
    if request.method == "POST":
        form = UserCreationFormCustom(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"index.html",{"mensaje":"Usuario Creado:)"})
        
    return render (request,"registro.html", {"form":form})