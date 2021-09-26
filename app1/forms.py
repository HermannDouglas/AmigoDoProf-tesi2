from django import forms
from app1.models import Aluno, Turma

class AlunoModelForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'numero_chamada']

class TurmaModelForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'ano_letivo']