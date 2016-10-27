from django.shortcuts import render, redirect,get_object_or_404
from CentroAsistencial.forms import ModelForm,ingresar
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from CentroAsist.models import Paciente, Profesional, RegistroHC, Adjuntos, PalabrasClave


def login(request):
    nombre = "Bienvendid@ al Centro Asistencial H3"
    form = ingresar()
    next_url = request.GET.get('next', '/')
    if request.method =="POST":
        form = ingresar(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect(request.POST.get('next', '/'))

    
        else: 
            form= Registrar()

    return render(request, 'login.html', 
        { 
        'nombre':nombre, 
         'form': form, 
        })


def logout(request):
    auth.logout(request)
    # redirect to a succes page
    return HttpResponseRedirect("/account/loggedout/")

def home(request):
    return render_to_response('login.html')

#def inicio():
    
    


#def registroHC():




#def Nuevo_Paciente():
