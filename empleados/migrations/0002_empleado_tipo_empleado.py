# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='tipo_empleado',
            field=models.CharField(choices=[('BASE', 'PERSONAL BASIFICADO'), ('CONF', 'PERSONAL DE CONFIANZA')], default='CONF', max_length=5),
        ),
    ]
