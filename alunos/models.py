from django.db import models
from datetime import date
class Aluno(models.Model):
    nome_completo= models.CharField(max_length=100)
    telefone= models.CharField(max_length=20, blank=True)
    email= models.EmailField(blank=True)
    cpf= models.CharField(max_length=14, blank=True)
    data_nascimento= models.DateField(blank=True)
    data_entrada= models.DateField(default=date.today)
    ativo= models.BooleanField(default=True)

class Meta:
    ordering = ["nome_completo"]

def __str__(self):
    return self.nome
