from django.shortcuts import render
from django.http import HttpResponse
from .models import Aluno

def inicio(request):
    contexto = {"nome_clube": "Evf Pagamentos"}
    return render(request, "alunos/inicio.html", contexto)

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render (request, "alunos/lista.html", {"alunos": alunos})