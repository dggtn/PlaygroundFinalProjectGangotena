from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from modelos.models import Post
from django.shortcuts import redirect


def posts(request):
    template = loader.get_template('posts.html')
    
    posts = Post.objects.all()
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