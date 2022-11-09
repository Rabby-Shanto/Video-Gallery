from django.urls import path
from .import views

urlpatterns = [
    path('', views.u_gallery,name='u_gallery'),
    path('create_playlist/',views.create_playlist.as_view(),name="create_playlist")
]
