from django.urls import path
from .views import message_list, message_detail
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from mensajes import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
  path('', views.index, name='mensajes_index'),
  path('nuevo', views.nuevo, name='mensajes_nuevo'),
  path('', message_list, name='message_list'),
  path('<int:pk>/', message_detail, name='message_detail')]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)