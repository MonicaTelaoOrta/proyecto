from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm

class UsuarioForm(UserCreationForm):
	username=forms.CharField(max_length=20, required=True, help_text=False, label="usuario")
	password2=forms.CharField(help_text=False,widget=forms.PasswordInput,label="contrasena(confirmar)"
	email=forms.EmailField(max_length=100, required=True,label="email")
	class Mata:
		model=User 
		fields=("username","password1","password2","email")
	def save(self,commit=True):
		user=super(UsuarioForm,self).save(commit=False)
		user.email=self.cleaned_data.get("email")
		if commit:
			user.save()
		return User 