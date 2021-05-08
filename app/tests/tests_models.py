from django.test import TestCase

from app.models import Filmes

class FilmesTestCase(TestCase):
    def setUp(self): #Cria um filme para teste
        Filmes.objects.create(
            titulo = "Gladiador",
            sinopse = "teste",
            generos = "Drama, Ação",
            duracao = "2h30",
            diretor = "Ridley Scott",
        )


    def test_titulo_max_length(self): #Testa se o titulo do filme possui menos de 50 letras
        filmes = Filmes.objects.get(id=1)
        max_length = filmes._meta.get_field('titulo').max_length
        nome = Filmes.objects.get(titulo='Gladiador')
        self.assertLess(len(nome.__str__()), max_length)