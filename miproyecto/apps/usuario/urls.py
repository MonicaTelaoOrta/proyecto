from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miproyecto.views.home', name='home'),
    url(r'^$', registro),
    url(r'^login/$', login)
)