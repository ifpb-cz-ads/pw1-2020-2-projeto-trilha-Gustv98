from django.contrib import admin
from .models import Filmes
# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_filter = ('usuario')

admin.site.register(Filmes)

