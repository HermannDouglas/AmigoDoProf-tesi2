from django.urls import path
from app1.views import index, turma, aluno

urlpatterns = [
    path('', index),
    path('turma', turma, name='turma'),
    path('aluno', aluno, name='aluno'),
]