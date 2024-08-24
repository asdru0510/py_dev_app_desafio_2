from django.db import models

# Create your models here.

class Tarea(models.Model):
    descripcion=models.TextField(default="")
    eliminada=models.BooleanField(default=False)

class Subtarea(models.Model):
    tarea_id = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='subtareas')
    descripcion=models.TextField(default="")
    eliminada=models.BooleanField(default=False)
