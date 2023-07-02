from django.urls import path
from .views import (
    index, 
    create_tarefa, 
    check_tarefa,
    uncheck_tarefa, 
    delete_tarefa, 
    edit_tarefa
)

urlpatterns = [
    path('', index, name='index'),
    path('category/<str:category>/', index, name='index'),
    path('create-tarefa/', create_tarefa, name='create_tarefa'),
    path('check-tarefa/<int:tarefa_id>/', check_tarefa, name='check_tarefa'),
    path('uncheck-tarefa/<int:tarefa_id>/', uncheck_tarefa, name='uncheck_tarefa'),
    path('delete-tarefa/<int:tarefa_id>/', delete_tarefa, name='delete_tarefa'),
    path('edit-tarefa/<int:tarefa_id>/', edit_tarefa, name='edit_tarefa'),
]