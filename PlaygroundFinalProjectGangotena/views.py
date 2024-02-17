from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from PlaygroundFinalProjectGangotena.form import UserCreationFormCustom,UserEditForm
from modelos.models import Post
from modelos.models import Usuarios
from modelos.models import Comentarios
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

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
    context = {
    'usuario': usuario,
  }
    return HttpResponse(template.render(context, request))
   
def publicar(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        autor = Usuarios(id= request.POST['id'] )
        cuerpo = request.POST['cuerpo']
        Post(titulo=titulo, cuerpo=cuerpo, autor=autor).save()
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


def nuevoComentario(request):
    template = loader.get_template('nuevoComentario.html')
    html = template.render(request=request)
    return HttpResponse(html)


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
            username = form.cleaned_data['username']
            form.save()
            usuario = Usuarios(nombre = form.cleaned_data['nombre'],apellido = form.cleaned_data['apellido'],apodo = form.cleaned_data['apodo'],pais = form.cleaned_data['pais'],email = form.cleaned_data['email'])
            usuario.save()
            return render(request,"index.html",{"mensaje":"Usuario Creado:)"})
            
    return render (request,"registro.html", {"form":form})

def editarPerfil(request):
    usuario= request.user
    if request.method =='POST':
       miFormulario = UserEditForm(request.POST, instance= request.user)

       if miFormulario.is_valid():
           if miFormulario.cleaned_data.get('imagen'):
               usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
               usuario.avatar.save()
           miFormulario.save()

           return render(request,"index.html")
    else:
        miFormulario = UserEditForm (initial={'imagen':usuario.avatar.imagen}, instance=request.user)
    return render(request, "editaPerfil.html",{"miFormulario":miFormulario,"usuario":usuario}) 

class CambiarContrasenia(LoginRequiredMixin,PasswordChangeView):
        template_name="cambiarContrasenia.html"
        succes_url = reverse_lazy('cambiarContrasenia')

