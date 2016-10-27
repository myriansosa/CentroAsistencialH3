from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from CentroAsist.models import Paciente, RegistroHC

#LOGIN
class ingresar(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }



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
