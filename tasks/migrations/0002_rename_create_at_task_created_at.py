# Generated by Django 5.1.4 on 2024-12-28 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='create_at',
            new_name='created_at',
        ),
    ]