from django.db import models



class Paciente(models.Model):

    NACIONALIDAD_CHOICES=(
        ('argentina', 'Argentino'),
        ('boliviana', 'Boliviano'),
        ('brasilera', 'Brasilera'),
        ('colombiana', 'Colombiano'),
        ('chilena', 'Chileno'),
        ('paraguaya','Paraguaya'),
        ('peruana','Peruano'),
        ('uruguaya', 'Uruguayo'),
        ('otra','otra'),
    )


    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    sexo = models.CharField(max_length=30, choices=(('m', 'masculino'), ('f', 'femenino')))
    fecha_nacimiento = models.DateField()
    dni = models.CharField(max_length=10, null=True, blank=True)
    domicilio= models.CharField(max_length=100,null=True, blank=True)

    nacionalidad=models.CharField(max_length= 25, choices=NACIONALIDAD_CHOICES, default=('argentina', 'Argentino'))

    familiares = models.ManyToManyField("self", symmetrical=True, blank=True)
    numero_hc = models.CharField(max_length=10,
                                 null=True, blank=True,
                                 help_text='Numero historia clinica en archivo físico')

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)


class Profesional(models.Model):
    user = models.OneToOneField('auth.User', related_name='profesional')
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    matricula=models.CharField(max_length=30)
    especialidad=models.CharField(max_length=30)


    def __str__(self):
        return "{} {} (MP {})".format(self.nombre, self.apellido, self.matricula)




class RegistroHC(models.Model):

    paciente=models.ForeignKey("Paciente")
    profesional = models.ForeignKey('Profesional', null=True)
    consulta=models.CharField(max_length=30)
    fecha=models.DateTimeField(auto_now=True)   # Almacena la fecha actual
    entrada=models.TextField(blank=True, null=True)


class Adjuntos(models.Model):
    registroHC=models.ForeignKey("RegistroHC")
    adjuntos=models.FileField(blank=True, null=True, upload_to="RegistroHC")


class PalabrasClave(models.Model):
    palabra=models.ManyToManyField("RegistroHC")
