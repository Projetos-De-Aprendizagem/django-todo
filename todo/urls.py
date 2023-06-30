from django.urls import path
from .views import index, create, check_tarefa


urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('check-tarefa/<int:tarefa_id>/', check_tarefa, name='check_tarefa'),
]