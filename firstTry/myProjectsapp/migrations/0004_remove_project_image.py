# Generated by Django 4.0.6 on 2022-07-24 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myProjectsapp', '0003_alter_project_options_alter_project_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
    ]