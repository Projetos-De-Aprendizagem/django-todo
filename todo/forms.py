from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['id', 'nome', 'categoria']

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        
        if len(nome) < 3:
            raise forms.ValidationError('O nome deve ter no mínimo 3 caracteres')
        return nome