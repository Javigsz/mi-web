from django.db import models

# Create your models here.
class Link(models.Model):

    name = models.CharField(max_length=200, verbose_name = "Título")
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de edición")
    url = models.URLField(verbose_name="Enlace", max_length = 200)

    class Meta:

        verbose_name = 'Link'
        verbose_name_plural = 'Link'
        ordering = ["-created"]

    def __str__(self):
        return self.name #Para que salga el titulo del proyecto en el admin y no "proyect 1"