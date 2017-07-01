# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad', models.CharField(max_length=4)),
                ('subunidad', models.CharField(max_length=4)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfc', models.CharField(max_length=13)),
                ('curp', models.CharField(max_length=18)),
                ('nombre', models.CharField(max_length=80)),
                ('paterno', models.CharField(max_length=80)),
                ('materno', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Plaza',
            fields=[
                ('clave', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nivel', models.CharField(max_length=4)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
    ]
