# Generated by Django 4.2.16 on 2024-10-18 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_responsible'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='responsible',
        ),
    ]