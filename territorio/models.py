from django.db import models

# Create your models here.

class Territorio(models.Model):
    idTerritorio = models.CharField(max_length=10)
    nombre = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
