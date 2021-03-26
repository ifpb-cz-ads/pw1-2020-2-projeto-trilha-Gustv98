from django.contrib import admin
from django.urls import path
from app import views
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page),

]
