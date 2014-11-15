from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *

urlpatterns = patterns('miproyecto.apps.usuario',
    # Examples:
    # url(r'^$', 'miproyecto.views.home', name='home'),
    url(r'^login/$', login),
    url(r'^registro/$', registro),
 	url(r'^comentarios/$',pagina_comentarios),
 	url(r'^inicio/$', inicio), 
 	url(r'^$', principal),   
)
