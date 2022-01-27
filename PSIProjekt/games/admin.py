from django.contrib import admin
from games.models import *
from django.contrib.admin import register


@register(Uzytkownik)
class UzytkownikAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
        'last_update',
    ]

@register(Producent)
class ProducentAdmin(admin.ModelAdmin):
    list_display = [
        'nazwa',
        'rok_zalozenia',
        'siedziba',
        'ilosc_czlonkow',
        'image',
    ]

@register(Gatunek)
class GatunekAdmin(admin.ModelAdmin):
    list_display = [
        'nazwa',
    ]

@register(Gra)
class GraAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'opis',
        'pegi',
        'ocena',
        'rok_produkcji',
        'idGatunku',
        'idProducenta',
        'price',
        'image',
    ]

@register(CartItem)
class CartItem(admin.ModelAdmin):
    list_display = [
        'order',
        'product',
        'quantity',
    ]