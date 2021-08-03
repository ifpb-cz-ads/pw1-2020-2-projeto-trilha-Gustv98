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
    path('login/', views.user_login, name="login"),
    path('login/submit', views.submit_login,name="checkLogin"),
    path('logout/', views.user_logout),
    path('addFavorito/', views.user_favorites),
    path('addFavorito/submit', views.submitUserFavorites),
    path('favoritos/delete/<int:id_filme>/', views.delete_filme),
    path('favoritos/', views.lista_favoritos, name="favoritos"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
