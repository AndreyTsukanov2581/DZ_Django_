# Generated by Django 5.0.4 on 2024-04-29 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='deccription',
            new_name='description',
        ),
    ]
