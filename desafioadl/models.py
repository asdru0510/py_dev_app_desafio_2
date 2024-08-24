from django.db import models

# Create your models here.

class Tarea(models.Model):
    description=models.TextField(default="")
    eliminada=models.BooleanField(default=False)

class Subtarea(models.Model):
    tarea_id = models.ForeignKey(Tarea, on_delete=models.CASCADE, related_name='subtarea')
    description=models.TextField(default="")
    eliminada=models.BooleanField(default=False)
