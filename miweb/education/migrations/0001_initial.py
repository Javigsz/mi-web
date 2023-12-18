# Generated by Django 4.2.7 on 2023-12-18 11:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('subtitle', models.CharField(max_length=500, verbose_name='Subtítulo')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Enlace')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('tools', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('courses', models.ManyToManyField(blank=True, to='education.course')),
            ],
        ),
    ]
