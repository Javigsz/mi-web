# Generated by Django 4.2.7 on 2023-12-18 12:49

import ckeditor.fields
from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Subtítulo')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('tools', models.TextField(verbose_name='Herramientas')),
                ('image', models.ImageField(upload_to='portfolio', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Enlace')),
                ('video', embed_video.fields.EmbedVideoField(default=None, null=True)),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'ordering': ['-created'],
            },
        ),
    ]