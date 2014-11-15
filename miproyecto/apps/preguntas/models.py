from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tema (models.Model):
	nombre_tema=models.CharField(max_length=50 , null=True)
 	def __unicode__(self):
 		return (self.nombre_tema)
class Pregunta(models.Model):
 	pregunta=models.CharField(max_length=200, null=True)
 	co_respuesta=models.CharField(max_length=200, null=True )
 	pregunta_m=models.ForeignKey(Tema)
class Respuesta(models.Model):
 	respuesta=models.CharField(max_length=200, null=True)
 	respuesta_m=models.ForeignKey(Pregunta)
 	def __unicode__(self):
 		return (self.respuesta)