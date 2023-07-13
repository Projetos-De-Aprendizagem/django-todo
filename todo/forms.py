from django import forms
from .models import Tarefa, Categoria

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
    