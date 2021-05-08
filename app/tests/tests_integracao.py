from django.test import TestCase ,Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from app.models import Filmes

class testePagina(TestCase):
    def teste_status(self): #Acessa a página com sucesso, pois não precisa estar logado
        response = self.client.get('login/')
        self.assertEquals(response.status_code, 200)

    def teste_status(self): #Redireciona pois o usuario não está logado
        response = self.client.get('/addFavorito/')
        self.assertEquals(response.status_code, 302)

    def setUp(self): #Cria usuario
        self.client = Client()
        self.user = User.objects.create_user('gustavo', 'gustavo@gmail.com', '123')

    def testLogin(self): #Página que necessita de login acessada com sucesso
        self.client.login(username='gustavo', password='123')
        response = self.client.get('/addFavorito/')
        self.assertEqual(response.status_code, 200)

    def logout(self):
        self.client.logout(username='gustavo', password='123')





