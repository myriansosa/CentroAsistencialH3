#ultimo


from django.shortcuts import render, redirect,get_object_or_404
from CentroAsistencial.forms import (LoginForm, PacienteForm, buscar, RegistroHCForm)
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from CentroAsist.models import Paciente, Profesional, RegistroHC, Adjuntos, PalabrasClave
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required


def login_view(request):
    nombre = "Bienvendid@ al Centro Asistencial H3"
    next_url = request.GET.get('next', '/')
    form = LoginForm(initial={'next_url': next_url})
    if request.method =="POST":
        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect(request.POST.get('next_url', '/'))
            else:
                form.add_error(None, 'usuario o contraseña incorrecto')

    return render(request, 'login.html', {'form': form,
            'nombre':nombre})


def logout(request):
    auth.logout(request)
    # redirect to a succes page
    return HttpResponseRedirect("/account/loggedout/")


@login_required
def home(request):
    return render_to_response('login.html')


@login_required
def registro_hc(request, id_paciente):
    paciente = get_object_or_404(Paciente, id=id_paciente)
    registros = RegistroHC.objects.filter(paciente=paciente).order_by('-fecha')
    print(registros)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegistroHCForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            registro = form.save(commit=False)
            registro.paciente = paciente
            registro.profesional = request.user.profesional
            registro.save()
            return redirect(request.path)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RegistroHCForm()

    return render(request, 'paciente.html',
                  {'form': form, 'paciente': paciente, 'registros': registros})


@login_required
def registro_paciente(request, id_paciente=None):
    # if this is a POST request we need to process the form data
    # paciente = get_object_or_404(Paciente, id=id_paciente)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PacienteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            paciente = form.save()
            return redirect('/paciente/{}'.format(paciente.id))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PacienteForm()

    return render(request, 'login.html', {'form': form})
