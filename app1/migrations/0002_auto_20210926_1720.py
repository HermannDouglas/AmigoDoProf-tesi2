# Generated by Django 3.2.7 on 2021-09-26 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='numero_chamada',
            field=models.IntegerField(max_length=99, verbose_name='Número chamada'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='ano_letivo',
            field=models.IntegerField(max_length=4, verbose_name='Ano letivo'),
        ),
        migrations.AlterField(
            model_name='turma',
            name='nome',
            field=models.CharField(max_length=15, verbose_name='Nome'),
        ),
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presente', models.BooleanField(default=False, verbose_name='Presente ?')),
                ('anotacao', models.CharField(max_length=300, verbose_name='Anotação: ')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.aluno')),
            ],
        ),
    ]