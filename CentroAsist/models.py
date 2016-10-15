from django.db import models



class Paciente(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    sexo = models.CharField(max_length=30, choices=(('m', 'masculino'), ('f', 'femenino')))
    fecha_nacimiento = models.DateField()
    dni = models.CharField(max_length=10, null=True, blank=True)
    domicilio= models.CharField(max_length=100,null=True, blank=True)
    id_familiar=models.IntegerField(unique=True)




class Profesional(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    matricula=models.CharField(max_length=30)
    especialidad=models.CharField(max_length=30)
    busqueda_HC=models.ForeignKey(RegistroHC)


class RegistroHC(models.Model):

    registro_paciente=models.ForeignKey(Paciente)
    consulta=models.CharField(max_length=30)
    fecha=models.DateField(auto_now=True) #Almacena la fecha actual
    Entrada=models.TextField()
    adjuntos=models.FileField(blank=True, null=True, upload_to=generate_path)


class Adjuntos(models.model):
	registroHC=models.ForeignKey(RegistroHC)


class PalabrasClave(models.Model):
    palabra=models.ManyToManyField(RegistroHC)
