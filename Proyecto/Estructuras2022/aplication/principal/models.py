from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Poster(models.Model):
    id = models.AutoField(primary_key = True)
    usuario = models.ForeignKey(User, on_delete = models.CASCADE)
    titulo = models.CharField(max_length = 70, null = False)
    precio = models.CharField(max_length = 100, null = False)
    etiqueta = models.CharField(max_length = 100, null = False)
    imagen = models.ImageField(upload_to = 'media/', default = 'post_1.JPG', null = False)


    def __str__(self) -> str:
        return self.titulo