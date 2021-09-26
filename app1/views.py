from django.contrib import messages
from django.shortcuts import render
from app1.forms import AlunoModelForm, TurmaModelForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def turma(request):
    if request.method == 'POST':
        form = TurmaModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Turma cadastrada com sucesso!')
        else:
            messages.error(request, 'Turma não cadastrada!')
    else:
        form = TurmaModelForm()
    context = {
        'form': form
    }
    return render(request, 'turma.html', context)

def aluno(request):
    if request.method == 'POST':
        form = AlunoModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno cadastrado com sucesso!')
        else:
            messages.error(request, 'Aluno não cadastrada!')
    else:
        form = AlunoModelForm()
    context = {
        'form': form
    }
    return render(request, 'aluno.html', context)