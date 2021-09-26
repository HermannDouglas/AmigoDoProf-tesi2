from django.db import models


class Turma(models.Model):

    nome = models.CharField('Nome: ', max_length=15)
    ano_letivo = models.IntegerField('Ano letivo: ', max_length=4)

    def __str__(self):
        return self.nome

class Aluno(models.Model):

    nome = models.CharField('Nome', max_length=100)

    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    numero_chamada = models.IntegerField('Número chamada: ', max_length=99)

    def __str__(self):

        return "{} {}".format(self.numero_chamada, self.nome)