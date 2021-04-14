from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse


# Create your models here.

class Filmes(models.Model):
    titulo = models.CharField(max_length=50)
    sinopse = models.TextField()
    image = models.ImageField(upload_to='images/')
    generos = models.CharField(max_length=80)
    duracao = models.CharField(max_length=30)
    diretor = models.CharField(max_length=50, null=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    favorite = models.ManyToManyField(User, related_name='filmes_favoritos', blank=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('favoritos')




