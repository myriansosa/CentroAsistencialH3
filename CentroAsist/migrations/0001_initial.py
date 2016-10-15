# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('sexo', models.CharField(max_length=30, choices=[('m', 'masculino'), ('f', 'femenino')])),
                ('fecha_nacimiento', models.DateField()),
                ('dni', models.CharField(null=True, max_length=30, blank=True)),
                ('domicilio', models.CharField(null=True, max_length=100, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PalabrasClave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('clave', models.CharField(null=True, max_length=20, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('matricula', models.CharField(max_length=30)),
                ('especialidad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroHC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('consulta', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
