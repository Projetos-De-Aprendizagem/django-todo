from django import forms
from .models import Tarefa, Categoria

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']

class TarefaForm(forms.ModelForm):
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget=forms.Select(attrs={'class': 'categoria'}))
    class Meta:
        model = Tarefa
        fields = ['nome', 'descricao', 'categoria']

        # Add similar style: .nome, .descricao, .categoria {...}
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'nome', 'placeholder': 'Adicione um nome'}),
            'descricao': forms.TextInput(attrs={'class': 'descricao', 'placeholder': 'Adicione uma descricao'}),
            'categoria': forms.TextInput(attrs={'class': 'categoria', 'placeholder': 'Categoria'}),
        }

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        
        if len(nome) < 3:
            raise forms.ValidationError('O nome deve ter no mínimo 3 caracteres')
        return nome
    
    def clean_descricao(self):
        descricao = self.cleaned_data['descricao']
        
        if len(descricao) < 10:
            raise forms.ValidationError('A descrição deve ter no mínimo 10 caracteres')
        return descricao


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'register_name', 'placeholder': 'Adicione um nome'}),
            'email': forms.TextInput(attrs={'class': 'register_email', 'placeholder': 'Adicione um email'}),
            'password1': forms.TextInput(attrs={'class': 'register_password', 'placeholder': 'Adicione um password'}),
            'password2': forms.TextInput(attrs={'class': 'register_password', 'placeholder': 'Confirme o password'}),
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'login_username', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'login_password', 'placeholder': 'Password'})
    )

