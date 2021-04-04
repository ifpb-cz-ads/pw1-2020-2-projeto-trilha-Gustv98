from django.db import models

# Create your models here.

class Filmes(models.Model):
    titulo = models.CharField(max_length=50)
    sinopse = models.TextField()
    image = models.ImageField(upload_to='images/')
    generos = models.CharField(max_length=80)
    duracao = models.CharField(max_length=30)
    diretor = models.CharField(max_length=50)

    def __str__(self):
        return self.titulo

