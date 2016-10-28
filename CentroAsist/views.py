#ultimo


from django.shortcuts import render, redirect,get_object_or_404
from CentroAsistencial.forms import (LoginForm, iniciar, buscar, añadirdatos)
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from CentroAsist.models import Paciente, Profesional, RegistroHC, Adjuntos, PalabrasClave
from django.template.response import TemplateResponse



def login_view(request):
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
            else:
                form.add_error(None, 'usuario o contraseña incorrecto')
    
    return render(request, 'login.html', {'form': form,
            'nombre':nombre})


def logout(request):
    auth.logout(request)
    # redirect to a succes page
    return HttpResponseRedirect("/account/loggedout/")

def home(request):
    return render_to_response('login.html')


#def inicio():


#def registroHC():




#def Nuevo_Paciente():
