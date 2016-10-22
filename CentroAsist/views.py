from django.shortcuts import render, redirect,get_object_or_404
from .forms import (loginForm)
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from CentroAsist.models import Paciente, Profesional, RegistroHC, Adjuntos, PalabrasClave


def login(request):
     nombre = "Bienvendid@ al Centro Asistencial H3"
    form = LoginForm()
    next_url = request.GET.get('next', '/')
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect(request.POST.get('next', '/'))

def logout(request):
    auth.logout(request)
    # redirect to a succes page
    return HttpResponseRedirect("/account/loggedout/")

def inicio():
    
    


def registroHC():




def Nuevo_Paciente():
