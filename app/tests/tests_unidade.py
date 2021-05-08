from django.test import TestCase ,Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from app.models import Filmes


class SigninTest(TestCase):

    def setUp(self): #Cria usuario e salva
        self.user = User.objects.create_user(username='test', password='12test12')
        self.user.save()

    def test_username_correto(self): #verifica se usuario está autenticado
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_username_incorreto(self): #verifica se nome ou senha estão incorretos
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)


class testView(TestCase):
    def setUp(self): #Cria um usuário para testar
        self.submit_login=reverse('checkLogin')
        self.login_url=reverse('login')
        self.user={
            'username': 'username',
            'password': 'password'
        }
        User.objects.create_user(**self.user)


class LoginTest(testView):
    def teste_acessar_pagina_de_login(self): #Teste se a página de login está usando o template correto
        response=self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def teste_login_realizado(self): #Testa se o usuario logou e se ele é redirecionado para a página correta
        response = self.client.post(self.submit_login, self.user, follow=True)
        self.assertTrue(response.context['user'].is_active)
        self.assertEquals(response.status_code, 200)
        self.assertRedirects(response, '/')



