from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


#LOGIN
def ingresar(Model.Form):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }



def iniciar(Model.Form):
    #CREAR Y BUSCAR PACIENTE
    class Meta:
        model=Paciente
        fields=['Nombre','Apellido','Historia Clinica','DNI']


def buscar(Model.Form):
    buscador = forms.CharField(max_length=40)

        

def añadirdatos(Model.Form):

    class Meta:
        model=RegistroHC
        fields=['Observaciones']