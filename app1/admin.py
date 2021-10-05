from django.contrib import admin
from app1.models import Turma, Aluno, Frequencia, Aula

# Register your models here.
admin.site.register(Turma)
admin.site.register(Aula)
admin.site.register(Aluno)
admin.site.register(Frequencia)
