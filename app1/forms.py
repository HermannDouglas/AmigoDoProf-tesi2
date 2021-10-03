from django import forms
from app1.models import Aluno, Turma, Frequencia


class AlunoModelForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'turma', 'numero_chamada']

class TurmaModelForm(forms.ModelForm):
    class Meta:
        model = Turma
        fields = ['nome', 'ano_letivo']

class FrequenciaModelForm(forms.ModelForm):
    class Meta:
        model = Frequencia
        fields = ['aluno', 'presente']

