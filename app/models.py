from django.db import models
from django.contrib.auth.models import User

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

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    nome = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nome



