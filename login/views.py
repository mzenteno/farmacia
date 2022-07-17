from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

def index(request, nombre):
    context  = {'nombre': nombre}
    return render(request, 'login/index.html', context)