from django.urls import path

from . import views

urlpatterns = [
    path('game', views.games_list, name='games_list'),
    path('ganre', views.genre_list, name='genre_list'),
    path('user', views.user_list, name='user_list'),
    path('producer', views.producer_list, name='producer_list'),
]