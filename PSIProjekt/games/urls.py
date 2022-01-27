from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('game', GameList.as_view()),
    path('game/<int:pk>', GameDetails.as_view()),
    path('ganre', GanreList.as_view()),
    path('user', UserList.as_view()),
    path('producer', ProducerList.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', ProducerListView.as_view(), name='producer_list'),
    path('producer/<int:id>/', GamesListView.as_view(), name='games_list'),
    path('register/', registerPage, name='register'),
    path('profil/', ProfilePage.as_view(), name='profile'),
    path('profil_update/', ProfileUpdate.as_view(), name='profile_update'),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)