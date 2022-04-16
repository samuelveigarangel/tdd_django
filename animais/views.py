from django.http import HttpResponse
from django.shortcuts import render
from animais.models import animal

def index(request):
    contexto = {'caracteristicas': animal.objects.all()}
    return render(request, 'index.html', contexto)
