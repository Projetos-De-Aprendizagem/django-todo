from django.shortcuts import render, redirect
from .forms import TarefaForm
from .models import Tarefa

# Create your views here.
def index(request):
    template = 'base.html'
    return render(request, template)

def create(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            descricao = form.cleaned_data['descricao']
            categoria = form.cleaned_data['categoria']

            tarefa = Tarefa(
                nome=nome,
                descricao=descricao, 
                categoria=categoria
            )
            tarefa.save()
            return redirect('index')
        else:
            print(form.errors)
    else:
        template = 'todo/form.html'
        tarefa_form = TarefaForm()
        contexto = {'form': tarefa_form}
    return render(request, template, contexto)