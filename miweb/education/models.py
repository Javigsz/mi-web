from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Course(models.Model):

    title = models.CharField(max_length=200, verbose_name = "Título")
    subtitle = models.CharField(max_length=500, verbose_name = "Subtítulo")
    link = models.URLField(verbose_name="Enlace", max_length = 200, null=True, blank=True)
    certificate = models.URLField(verbose_name="Certificado", max_length = 200, null=True, blank=True)

    def __str__(self):
        return self.title #Para que salga el titulo del proyecto en el admin y no "proyect 1"


class Language(models.Model):

    title = models.CharField(max_length=200, verbose_name = "Título")
    tools = RichTextField(verbose_name="Contenido")
    courses = models.ManyToManyField(Course, blank=True, related_name="courses", null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de edición")

    def __str__(self):
        return self.title #Para que salga el titulo del proyecto en el admin y no "proyect 1"