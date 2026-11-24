from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ["nome_completo", "telefone", "email", "cpf", "data_nascimento", "data_entrada", "ativo"]
    list_filter = ["ativo"]
    search_fields = ["nome", "telefone", "email", "cpf", "data_nascimento", "data_entrada"]