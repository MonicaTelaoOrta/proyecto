from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def login(request):
	if request.method=="POST":
		form=AuthenticationForm(request.POST)
		if form.is_valid()== False:
			username=request.POST["username"]
			password=request.POST["password"]
			resultado=authenticate(username=username,password=password)
			if resultado:
				login(request,resultado)
				request.session["name"]=username
				return HttpResponseRedirect("//")
	form=AuthenticationForm()
	return render_to_response("usuario/login.html",{"form":form},RequestContext(request))

def logout(request):
	logout(request)
	return HttpResponseRedirect("")

def registro(request):
	if request.method=="POST":
		formulario =UsuarioForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("")
	formulario=UsuarioForm()
	return render_to_response("usuario/registro.html",{"formulario":formulario},RequestContext(request))
def pagina_comentarios(request):
	if request.method=="POST":
		formulario =UsuarioForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect("")
	formulario=UsuarioForm()
	return render_to_response("includes/comentarios.html",{"comentarios":formulario},RequestContext(request))
def inicio(request):
	return render_to_response("principal/inicio.html",RequestContext(request))
def principal(request):
	return render_to_response("principal/principal.html",RequestContext(request))
		
	

