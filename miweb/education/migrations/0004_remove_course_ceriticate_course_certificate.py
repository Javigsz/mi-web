# Generated by Django 4.2.7 on 2023-12-18 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0003_course_ceriticate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='ceriticate',
        ),
        migrations.AddField(
            model_name='course',
            name='certificate',
            field=models.URLField(blank=True, null=True, verbose_name='Certificado'),
        ),
    ]
