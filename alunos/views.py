from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Aluno
from .forms import AlunoForm

def inicio(request):
    contexto = {"nome_clube": "Evf Pagamentos"}
    return render(request, "alunos/inicio.html", contexto)

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render (request, "alunos/lista.html", {"alunos": alunos})

def cadastrar_aluno(request):
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_alunos")
    else:
        form = AlunoForm()

    return render(request, "alunos/form.html", {"form": form})