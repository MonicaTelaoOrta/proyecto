from django import forms
from .models import *
from django.forms import ModelForm

class TemaForm(ModelForm):
	class Meta:
		model=Tema
class PreguntaForm(ModelForm):
	class Meta:
		model=Pregunta
		exclude=['pregunta_m']
class RespuestaForm(ModelForm):
	class Meta:
		model=Respuesta
		exclude=['respuesta_m']
