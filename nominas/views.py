# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/login/")
def index(request):
    return render(request, "nominas/index.html",{})
