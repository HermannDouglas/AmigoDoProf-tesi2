from django.urls import path
from app1.views import index, turma, aluno, frequencia, aluno_list

urlpatterns = [
    path('', index),
    path('turma', turma, name='turma'),
    path('aluno', aluno, name='aluno'),
    path('frequencia', frequencia, name='frequencia'),
    path('aluno_list', aluno_list, name='aluno_list'),
]