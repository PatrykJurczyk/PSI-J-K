from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Uzytkownik(AbstractUser):
    last_update = models.DateTimeField(auto_now_add=True)



class Producent(models.Model):
    nazwa = models.CharField(max_length=45, blank=False, null=False)
    rok_zalozenia = models.DateField()
    siedziba = models.CharField(max_length=45, blank=False, null=False)
    ilosc_czlonkow = models.IntegerField()
    image = models.ImageField('Zdjęcie', blank=True)

    def __str__(self):
        return self.nazwa


class Gatunek(models.Model):
    nazwa = models.CharField(max_length=45, blank=False, null=False)
    def __str__(self):
        return self.nazwa


class Gra(models.Model):
    name = models.CharField(max_length=20, blank=False)
    opis = models.CharField(max_length=200, blank=False)
    pegi = models.CharField(max_length=20, blank=False)
    ocena = models.CharField(max_length=20, blank=False)
    price = models.FloatField('Cena Gry', default=0, blank=True)
    image = models.ImageField('Zdjęcie', blank=True)
    rok_produkcji = models.DateField()
    idGatunku = models.ForeignKey(Gatunek, null=False, blank=False, on_delete=models.DO_NOTHING)
    idProducenta = models.ForeignKey(Producent, null=False, blank=False, on_delete=models.DO_NOTHING)


class Order(models.Model):
    name = models.CharField('Imię i Nazwisko', max_length=200, default='', blank=True)
    address = models.CharField('Adres', max_length=200, default='', blank=True)
    address_client = models.ForeignKey(
        Uzytkownik,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='client',
    )

    def __str__(self):
        return f'Zamówienie #{self.id}'



class CartItem(models.Model):
    order = models.ForeignKey(
        Order,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    product = models.ForeignKey(
        Gra,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
    quantity = models.IntegerField('Ilosc')