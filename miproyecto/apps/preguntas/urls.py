from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *

urlpatterns = patterns('miproyecto.apps.preguntas',
    # Examples:
    # url(r'^$', 'miproyecto.views.home', name='home'),
    url(r'^tema/$', tema),
    url(r'^pregunta/$', pregunta),
 	url(r'^respuesta/$',respuesta),   
)