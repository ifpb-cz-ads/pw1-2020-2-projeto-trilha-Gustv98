from django.shortcuts import render, redirect
from app.models import Filmes
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView
from django import forms

# Create your views here.

class HomeView(ListView):
    model = Filmes
    template_name = 'home.html'


@login_required(login_url='/login/')
def submitUserFavorites(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        sinopse = request.POST.get('sinopse')
        generos = request.POST.get('generos')
        duracao = request.POST.get('duracao')
        diretor = request.POST.get('diretor')
        usuario = request.user
        id_filme = request.POST.get('id_filme')
        if id_filme:
            Filmes.objects.filter(id=id_filme).update(titulo=titulo,
                                                     sinopse=sinopse,
                                                      generos=generos,
                                                      duracao=duracao,
                                                      diretor=diretor)
        else:
            Filmes.objects.create(titulo=titulo,
                                sinopse=sinopse,
                                generos=generos,
                                duracao=duracao,
                                diretor=diretor,
                                usuario=usuario)
            
    return render(request, 'add_favorito.html')

def user_login(request):
    return render(request, 'login.html')

@login_required(login_url='login/')
def user_favorites(request):
    return render(request, 'add_favorito.html')


def lista_favoritos(request):
    usuario = request.user
    filme = Filmes.objects.filter(usuario=usuario)
    dados = {'filmes': filme}
    return render(request, 'favoritos.html', dados)

def user_logout(request):
    logout(request)
    return redirect('/login/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect('/login/')


