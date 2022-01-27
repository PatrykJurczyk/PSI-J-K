from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import *
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

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
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
       views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
       views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('koszyk/', views.cart_detail, name='cart_detail'),
    path('platnosc/', PaymentPage.as_view(), name='payment_page'),
    path('sukces/', SuccessOrder.as_view(), name='success_order'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)