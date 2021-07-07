from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripccion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creacion") #Se anade la hora de creacion
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado") #Se actualiza la hora de modificacion
    link = models.URLField(verbose_name="Link", blank=True, null=True)

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created']

    def __str__(self):
        return self.title