# Generated by Django 4.2.2 on 2023-06-24 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='descricao',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
