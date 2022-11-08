from django.urls import path
from .import views

urlpatterns = [
    path('', views.u_gallery,name='u_gallery'),
]
