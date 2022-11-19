
from django.contrib import admin
from django.urls import path,include
from VideoGallery import settings
from .import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('user_gallery/',include('UserGallery.urls')),
    path('accounts/', include('allauth.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
