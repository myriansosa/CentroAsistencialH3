from django.db import models



class Paciente(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    sexo = models.CharField(max_length=30, choices=(('m', 'masculino'), ('f', 'femenino')))
    fecha_nacimiento = models.DateField()
    dni = models.CharField(max_length=10, null=True, blank=True)
    domicilio= models.CharField(max_length=100,null=True, blank=True)
    nacionalidad=models.ChoiceField(NACIONALIDAD_CHOICES = (
        
        ('argentina', 'Argentino'),
        ('boliviana', 'Boliviano'),
        ('chilena', 'Chileno'),
        ('paraguaya','Paraguaya'),
        ('peruana','Peruano'),
        ('uruguaya', 'Uruguayo'),
        ('brasilera', 'Brasilera'),
        ('colombiana', 'Colombiano'),
        ('otra','otra'),)

    id_familiar=models.ManyToManyField("self")
    familiares = models.ManyToManyField("self", symmetrical=True)



class Profesional(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    matricula=models.CharField(max_length=30)
    especialidad=models.CharField(max_length=30)
    busqueda_HC=models.ForeignKey("RegistroHC")


class RegistroHC(models.Model):

    registro_paciente=models.ForeignKey("Paciente")
    consulta=models.CharField(max_length=30)
    fecha=models.DateField(auto_now=True) #Almacena la fecha actual
    entrada=models.TextField()
    

class Adjuntos(models.model):
	registroHC=models.ForeignKey("RegistroHC")
	adjuntos=models.FileField(blank=True, null=True, upload_to=generate_path)


class PalabrasClave(models.Model):
    palabra=models.ManyToManyField("RegistroHC")
