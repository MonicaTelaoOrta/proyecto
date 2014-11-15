from django.conf.urls import patterns, include, url
from django.contrib import admin
from django import forms
from miproyecto.apps.usuario.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miproyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include("miproyecto.apps.usuario.urls")),
    url(r'^', include("miproyecto.apps.preguntas.urls")),


)