# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from empleados.models import Empleado


# Create your views here.
@login_required(login_url="/login/")
def index(request):
    empleados = Empleado.objects.all()
    return render(request, "empleados/index.html",{ 'empleados' : empleados})