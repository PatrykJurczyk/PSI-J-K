from django.db import models

# Create your models here.

class Uzytkownik(models.Model):
    imie = models.CharField(max_length=45, blank=False, null=False)
    nazwisko = models.CharField(max_length=45, blank=False, null=False)
    email = models.CharField(max_length=50)
    aktywny = models.BooleanField(default=False)
    last_update = models.DateTimeField(auto_now_add=True)

class Producent(models.Model):
    nazwa = models.CharField(max_length=45, blank=False, null=False)
    rok_zalozenia = models.DateField()
    siedziba = models.CharField(max_length=45, blank=False, null=False)
    ilosc_czlonkow = models.IntegerField()

class Gatunek(models.Model):
    nazwa = models.CharField(max_length=45, blank=False, null=False)

class Gra(models.Model):
    tytul = models.CharField(max_length=20, blank=False)
    opis = models.CharField(max_length=20, blank=False)
    pegi = models.CharField(max_length=20, blank=False)
    ocena = models.CharField(max_length=20, blank=False)
    rok_produkcji = models.DateField()
    idUzytkownika = models.ForeignKey(Uzytkownik, null=False, blank=False, on_delete=models.DO_NOTHING)
    idGatunku = models.ForeignKey(Gatunek, null=False, blank=False, on_delete=models.DO_NOTHING)
    idProducenta = models.ForeignKey(Producent, null=False, blank=False, on_delete=models.DO_NOTHING)