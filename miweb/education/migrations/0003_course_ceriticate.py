# Generated by Django 4.2.7 on 2023-12-18 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_alter_language_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='ceriticate',
            field=models.URLField(blank=True, null=True, verbose_name='Enlace'),
        ),
    ]