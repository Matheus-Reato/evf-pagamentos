from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ["nome_completo", "telefone", "email", "cpf", "data_nascimento", "ativo", "data_entrada"]
        widgets = {
            "data_nascimento": forms.DateInput(
                            attrs={"type": "date"}, format="%Y-%m-%d"
                        ),

            "data_entrada": forms.DateInput(
                attrs={"type": "date"}, format="%Y-%m-%d"
            ),
        }