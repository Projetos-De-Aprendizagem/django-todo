from django.shortcuts import render, redirect, get_object_or_404
from .forms import TarefaForm
from .models import Tarefa, Categoria

from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request, category='all'):
    categorias = Categoria.objects.all()

    # tarefa filtrada pelo usuario
    tarefas = Tarefa.objects.filter(usuario=request.user.id)

    numero_tarefas_feitas = Tarefa.objects.filter(feito=True, usuario=request.user).count()
    numero_tarefas_nao_feitas = Tarefa.objects.filter(feito=False, usuario=request.user).count()

    if category == 'done':
        tarefas = tarefas.filter(feito=True)
    elif category == 'todo':
        tarefas = tarefas.filter(feito=False)

    contexto = {
        'tarefas': tarefas,
        'categorias': categorias,
        'numero_tarefas_feitas': numero_tarefas_feitas,
        'numero_tarefas_nao_feitas': numero_tarefas_nao_feitas,
        'selected_category': category
    }
    template = 'todo/main.html'
    return render(request, template, contexto)


@login_required
def check_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    # deixar a tarefa como feita.
    tarefa.feito = True
    tarefa.save()
    return redirect('index')


@login_required
def uncheck_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    # deixar a tarefa como feita.
    tarefa.feito = False
    tarefa.save()
    return redirect('index')


@login_required
def create_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            descricao = form.cleaned_data['descricao']
            categoria = form.cleaned_data['categoria']

            tarefa = Tarefa(
                nome=nome,
                descricao=descricao,
                categoria=categoria,
                # adicionado usuario automaticamente.
                usuario=request.user
            )
            tarefa.save()
            return redirect('index')
    else:
        form = TarefaForm()

    template = 'todo/form.html'
    contexto = {'form': form}
    return render(request, template, contexto)

@login_required
def delete_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.delete()
    return redirect('index')


@login_required
def edit_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)

    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TarefaForm(instance=tarefa)

    # added this variable to change form button.
    edit = True
    template = 'todo/form.html'
    contexto = {'form': form, 'tarefa_id': tarefa_id, 'edit':edit}
    return render(request, template, contexto)


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserRegistrationForm()
    template = 'todo/auth_form.html'
    contexto = {'form': form, 'view_name':'register'}
    return render(request, template, contexto)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to the home page after successful login
            else:
                # Handle authentication error
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    template = 'todo/auth_form.html'
    contexto = {'form': form, 'view_name':'login'}
    return render(request, template, contexto)

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')