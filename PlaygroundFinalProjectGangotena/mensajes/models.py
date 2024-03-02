from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chat(models.Model):
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    participante_uno = models.OneToOneField(User, on_delete=models.CASCADE, related_name="participante_uno")
    participante_dos = models.OneToOneField(User, on_delete=models.CASCADE, related_name="participante_dos")

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)