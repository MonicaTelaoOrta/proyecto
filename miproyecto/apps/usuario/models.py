from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.db import connection
# Create your models here.
class Categorias(models.Model):
	nombre=models.CharField(max_length=100)
class Comentario(models.Model):
	Contenido=models.TextField()
	fecha=models.DateField(auto_now=True)
	