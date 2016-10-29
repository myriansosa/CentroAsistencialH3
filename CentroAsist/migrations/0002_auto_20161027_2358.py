# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-27 23:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CentroAsist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adjuntos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adjuntos', models.FileField(blank=True, null=True, upload_to='RegistroHC')),
            ],
        ),
        migrations.RemoveField(
            model_name='palabrasclave',
            name='clave',
        ),
        migrations.AddField(
            model_name='paciente',
            name='familiares',
            field=models.ManyToManyField(related_name='_paciente_familiares_+', to='CentroAsist.Paciente'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='id_familiar',
            field=models.ManyToManyField(related_name='_paciente_id_familiar_+', to='CentroAsist.Paciente'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='nacionalidad',
            field=models.CharField(choices=[('argentina', 'Argentino'), ('boliviana', 'Boliviano'), ('brasilera', 'Brasilera'), ('colombiana', 'Colombiano'), ('chilena', 'Chileno'), ('paraguaya', 'Paraguaya'), ('peruana', 'Peruano'), ('uruguaya', 'Uruguayo'), ('otra', 'otra')], default=('argentina', 'Argentino'), max_length=25),
        ),
        migrations.AddField(
            model_name='palabrasclave',
            name='palabra',
            field=models.ManyToManyField(to='CentroAsist.RegistroHC'),
        ),
        migrations.AddField(
            model_name='profesional',
            name='busqueda_HC',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CentroAsist.RegistroHC'),
        ),
        migrations.AddField(
            model_name='registrohc',
            name='entrada',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registrohc',
            name='registro_paciente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CentroAsist.Paciente'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='dni',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='registrohc',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='adjuntos',
            name='registroHC',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CentroAsist.RegistroHC'),
        ),
    ]
