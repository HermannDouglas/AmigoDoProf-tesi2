from django.db import models


class Turma(models.Model):

    nome = models.CharField('Nome: ', max_length=15)
    ano_letivo = models.IntegerField('Ano letivo: ', max_length=4)

    def __str__(self):
        return self.nome

