from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from mensajes import models
# Create your views here.

def message_list(request):
    messages = models.Message.objects.all()
    return render(request, 'message_list.html', {'messages': messages})

def message_detail(request, pk):
    message = get_object_or_404(models.Message, pk=pk)
    return render(request, 'message_detail.html', {'message': message})
