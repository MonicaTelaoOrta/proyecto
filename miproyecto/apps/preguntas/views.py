from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect 
from .models import *
from .forms import *
import pdb

def tema(request):
	if (request.method=="POST"):
		form_tema=TemaForm(request.POST)
		if (form_tema.is_valid()):
			tema=request.POST["nombre_tema"]
			request.session["tema"]=tema
			form_tema.save()
			return HttpResponseRedirect("/pregunta/")
	else:
		form_tema=TemaForm()
	return render_to_response("tema/tema.html",{"form_tema":form_tema},RequestContext(request))

def pregunta(request):
	if (request.method=="POST"):
		form_pregunta=PreguntaForm(request.POST)
		nombre_tem=Tema.objects.get(nombre_tema=request.session["tema"])
		if (form_pregunta.is_valid()):
			pregunta_m=request.POST["pregunta"]
			request.session["pregunta"]=pregunta_m
			tem=form_pregunta.save(commit=False)
			tem.pregunta_m=nombre_tem
			#pdb.set_trace()
			tem.save()
			return HttpResponseRedirect("/respuesta/")
	else:
		form_pregunta=PreguntaForm()
	return render_to_response("tema/pregunta.html",{"form_pregunta":form_pregunta},RequestContext(request))

def respuesta(request):
	if (request.method=="POST"):
		form_respuesta=RespuestaForm(request.POST)
		nombre_pre=Pregunta.objects.get(pregunta=request.session["pregunta"])
		if (form_respuesta.is_valid()):
			re_pregunta=form_respuesta.save(commit=False)
			re_pregunta.respuesta_m=nombre_pre
			re_pregunta.save()
			return HttpResponseRedirect("/respuesta/")
	else:
		form_respuesta=RespuestaForm()
	return render_to_response("tema/respuesta.html",{"form_respuesta":form_respuesta},RequestContext(request))

# Create your views here.
