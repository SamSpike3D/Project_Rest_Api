from django.db import models

# Create your models here.
class Project(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion=models.TextField()
    tecnologia=models.CharField(max_length=200)
    fechacrt = models.DateTimeField(auto_now_add=True)