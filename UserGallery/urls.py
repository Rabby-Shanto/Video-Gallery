from django.urls import path
from .import views

urlpatterns = [
    path('', views.u_gallery,name='u_gallery'),
    path('create_playlist/',views.create_playlist.as_view(),name="create_playlist"),
    path('details/<int:pk>',views.detail_view.as_view(),name="detail"),
    path('update/<int:pk>',views.update_playlist.as_view(),name="update"),
    path('delete/<int:pk>',views.delete_playlist.as_view(),name="delete"),

    path('<int:pk>/addvideo',views.add_video,name="add_video")
]
