# Generated by Django 4.0.6 on 2022-07-25 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myProjectsapp', '0005_category_project_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]