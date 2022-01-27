from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('game', views.GameList.as_view()),
    path('game/<int:pk>', views.GameDetails.as_view()),
    path('ganre', views.GanreList.as_view()),
    path('user', views.UserList.as_view()),
    path('producer', views.ProducerList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)