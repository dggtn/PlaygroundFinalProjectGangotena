from django.contrib import admin
from modelos import models
admin.site.register(models.Usuarios)
admin.site.register(models.Comentarios)
admin.site.register(models.Avatar)
admin.site.register(models.Post)

# Register your models here.
