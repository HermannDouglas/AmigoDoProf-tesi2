from django import forms
from app1.models import Aluno, Turma, Frequencia, Aula


class TurmaModelForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'ano_letivo']

class AulaModelForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ['conteudo', 'data']

class AlunoModelForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'turma', 'numero_chamada']

class FrequenciaModelForm(forms.ModelForm):
    class Meta:
        model = Frequencia
        fields = ['aluno', 'presente', 'aula']


