from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("lista/", views.lista_alunos, name="lista_alunos"),
    path("novo/", views.cadastrar_aluno, name="cadastrar_aluno")
]