from django.contrib import admin
from django.urls import path
from app import views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index_page),
    path('favoritos/', views.favoritos),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
