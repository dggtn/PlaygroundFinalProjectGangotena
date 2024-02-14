from django.http import HttpResponse
from django.template import loader
from modelos.models import Post
from modelos.models import Usuarios
from modelos.models import Comentarios
from django.shortcuts import redirect


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
    
    usuarios = Usuarios.objects.all()
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