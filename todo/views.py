from django.shortcuts import render, redirect, get_object_or_404
from .forms import TarefaForm
from .models import Tarefa, Categoria

# Create your views here.
def index(request):
    categorias = Categoria.objects.all()
    tarefas = Tarefa.objects.all()
    numero_tarefas_feitas = Tarefa.objects.filter(feito=True).count()
    numero_tarefas_nao_feitas = Tarefa.objects.filter(feito=False).count()
    contexto = {
        'tarefas': tarefas, 
        'categorias': categorias, 
        'numero_tarefas_feitas': numero_tarefas_feitas, 
        'numero_tarefas_nao_feitas': numero_tarefas_nao_feitas
    }
    template = 'todo/main.html'
    return render(request, template, contexto)

def check_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    # fazer a tarefa como feita.
    tarefa.feito = True
    tarefa.save()
    return redirect('index')

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