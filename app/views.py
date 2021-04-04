from django.shortcuts import render
from app.models import Filmes

# Create your views here.

def index_page(request):
    evento = Filmes.objects.all()
    dados = {'eventos' :evento}
    return render(request, 'index.html', dados)

