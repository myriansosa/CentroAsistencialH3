from django.contrib import admin
from CentroAsist.models import Paciente, Profesional, RegistroHC, PalabrasClave, Adjuntos


admin.site.register(Paciente)
admin.site.register(Profesional)
admin.site.register(RegistroHC)
admin.site.register(PalabrasClave)
admin.site.register(Adjuntos)
