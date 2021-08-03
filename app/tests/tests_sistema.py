from django.test import TestCase ,Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from app.models import Filmes

class TesteFilmes(TestCase):
    @classmethod
    def setUp(cls):
        Filmes.objects.create(
            titulo = "Teste",
            sinopse = "teste",
            generos = "Drama",
            duracao = "2h30",
            diretor = "Ridley Scott",
        )

        Filmes.objects.create(
            titulo = "Teste2",
            sinopse = "teste",
            generos = "Drama, Mais drama",
            duracao = "2h45",
            diretor = "Gustavo",
        )
    
    def teste_filme(self):
        filme = Filmes.objects.get(id=1)
        filme_titulo_esperado = filme.titulo
        self.assertEquals(filme_titulo_esperado, 'Teste')

    def teste_filme2(self):
        filme = Filmes.objects.get(id=2)
        filme_titulo_esperado = filme.titulo
        self.assertEquals(filme_titulo_esperado, 'Teste2')



    
    

    