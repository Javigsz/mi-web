from django.db import models
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField

# Create your models here.
class Project(models.Model):

    title = models.CharField(max_length=200, verbose_name = "Título")
    subtitle = models.CharField(max_length=200, verbose_name = "Subtítulo")
    content = RichTextField(verbose_name="Contenido")
    tools = models.TextField(verbose_name = "Herramientas")
    image = models.ImageField(verbose_name = "Imagen",upload_to="portfolio")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de edición")
    link = models.URLField(verbose_name="Enlace", max_length = 200, null=True, blank=True)
    video = EmbedVideoField(null=True)

    class Meta:

        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ["-created"]

    def __str__(self):
        return self.title #Para que salga el titulo del proyecto en el admin y no "proyect 1"
