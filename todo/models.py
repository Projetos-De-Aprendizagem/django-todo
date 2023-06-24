from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nome)

class Tarefa(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=40, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.nome)
