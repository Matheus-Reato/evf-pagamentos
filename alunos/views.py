from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    contexto = {"nome_clube": "Evf Pagamentos"}
    return render(request, "alunos/inicio.html", contexto)