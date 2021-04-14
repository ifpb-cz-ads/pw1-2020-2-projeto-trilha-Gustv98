from django.contrib import admin
from django.urls import path
from app import views
from app.views import HomeView
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('login/', views.user_login),
    path('login/submit', views.submit_login),
    path('logout/', views.user_logout),
    path('addFavorito/', views.submitUserFavorites),
    path('addFavorito/submit', views.submitUserFavorites),
    path('favoritos/', views.lista_favoritos, name="favoritos"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
