# Generated by Django 4.2.2 on 2023-06-30 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_tarefa_is_done'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefa',
            old_name='is_done',
            new_name='feito',
        ),
    ]
