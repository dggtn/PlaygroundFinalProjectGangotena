from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from PlaygroundFinalProjectGangotena.form import PostCreation, UserCreationFormCustom
from modelos.models import Post
from modelos.models import Comentarios
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User

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
    template = loader.get_template('nuevoPost.html')
    form =  PostCreation(initial={'autor':request.user.id})
    context = {
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
        usuarios = User.objects.all()
    else:
        usuarios= User.objects.filter(first_name__icontains=query)

    contexto = {
        'usuarios': usuarios
    }
    html = template.render(contexto, request)
    return HttpResponse(html)


def usuarioPorId(request,id):
  usuarioPorId = User.objects.get(pk=id)
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
        formCrearUsuario = UserCreationFormCustom(request.POST)
        if formCrearUsuario.is_valid():
            nuevoUsuario = formCrearUsuario.save()
    return redirect('usuarios')


def nuevoComentario(request):
    usuario = User.objects.get(email= request.user.email)
    template = loader.get_template('nuevoComentario.html')
    context = {
    'usuario': usuario,
  }
    return HttpResponse(template.render(context, request))


def comentar(request):
    if request.method == 'POST':
        cuerpo = request.POST['cuerpo']
        user = User(id=request.user.id)
        post = Post(id = request.POST['post_id'] )
        Comentarios(autor=user, cuerpo=cuerpo, post=post).save()
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
            return render(request, "index.html")
    return render(request, "login.html", {"form":form})

def register(request):
    form = UserCreationFormCustom()
    if request.method == "POST":
        form = UserCreationFormCustom(request.POST)
        if form.is_valid():
            user = form.save()
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

def mensajeria(request):
    template = loader.get_template('mensajeria.html')
    contexto = {
        'usuarios': User.objects.all()
    }
    return HttpResponse(template.render(contexto, request))
