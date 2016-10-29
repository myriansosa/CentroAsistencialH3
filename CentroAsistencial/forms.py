from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, Form
from CentroAsist.models import Paciente, RegistroHC

#LOGIN
class LoginForm(Form):
    username = forms.CharField(max_length=40, label="Nombre de usuario")
    password = forms.CharField(widget=forms.PasswordInput(), label="Contraseña")


class iniciar(ModelForm):
    #CREAR Y BUSCAR PACIENTE
    class Meta:
        model= Paciente
        fields=['nombre','apellido','dni']


class buscar(ModelForm):
    buscador = forms.CharField(max_length=40)

        

class añadirdatos(ModelForm):

    class Meta:
        model=RegistroHC
        fields=['registro_paciente']
