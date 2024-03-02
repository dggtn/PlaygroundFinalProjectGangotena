import datetime
from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from mensajes import models
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.

def buscar_chat(usuario_emisor, usuario_contactado):
    q1 = Q(participante_uno=usuario_emisor.id)
    q2 = Q(participante_dos=usuario_contactado.id)
    q3 = Q(participante_uno=usuario_contactado.id)
    q4 = Q(participante_dos=usuario_emisor.id)
    try:
        chat = models.Chat.objects.get((q1 & q2) | (q3 & q4))
        mensajes = chat.message_set.all()
    except:
        chat = None
        mensajes = []
    return chat, mensajes

def index(request):
    usuarios = User.objects.exclude(id = request.user.id)
    id_contacto = request.GET.get('id_contacto')
    if id_contacto:
        usuario_contactado = User.objects.get(pk=id_contacto)
    else:
        usuario_contactado = usuarios[0]
    chat, mensajes = buscar_chat(request.user, usuario_contactado)
    contexto = { 'usuarios': usuarios, 'usuario_contactado': usuario_contactado, 'chat': chat, 'mensajes': mensajes}
    return render(request, 'mensajes/index.html', contexto)

def nuevo(request):
    if request.method == "POST":
        emisor_id = request.POST['emisor_id']
        receptor_id = request.POST['receptor_id']
        mensaje = request.POST['mensaje']
        fecha = datetime.datetime.now()

        emisor = User(id = emisor_id)
        receptor = User(id = receptor_id)

        if 'chat_id' in request.POST:
            chat = models.Chat.objects.get(pk=request.POST['chat_id'])
        else:
            chat = models.Chat.objects.create(fecha_inicio=fecha, participante_uno=emisor, participante_dos=receptor)

        chat.message_set.create(sender=emisor, receiver=receptor, body=mensaje, created_at=fecha)
        return redirect(reverse('mensajes_index') + '?id_contacto=' + receptor_id)

def message_list(request):
    messages = models.Message.objects.all()
    return render(request, 'message_list.html', {'messages': messages})

def message_detail(request, pk):
    message = get_object_or_404(models.Message, pk=pk)
    return render(request, 'message_detail.html', {'message': message})