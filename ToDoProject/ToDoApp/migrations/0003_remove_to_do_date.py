# Generated by Django 3.0.8 on 2022-07-17 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0002_auto_20220717_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='to_do',
            name='date',
        ),
    ]
