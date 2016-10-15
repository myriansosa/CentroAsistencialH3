from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm



def registrar(ModelForm):
	class Meta:
		model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
	


def iniciar(forms.Form):
	