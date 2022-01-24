from django.db import models

# Create your models here.

class Jezyk(models.Model):
    nazwa = models.CharField(max_length=20, blank=False)
    last_update = models.DateTimeField(auto_now_add=True)

class Gra(models.Model):
    tytul = models.CharField(max_length=255, blank=False)
    opis = models.TextField()
    rok_wydania = models.DateField()
    cena = models.DecimalField(max_digits=4, decimal_places=2)
    PEGI3 = 'Pegi-3'
    PEGI7 = 'Pegi-7'
    PEGI12 = 'Pegi-12'
    PEGI16 = 'Pegi-16'
    PEGI18 = 'Pegi-18'
    AGE = (
        (PEGI3, 'Pegi-3'),
        (PEGI7, 'Pegi-7'),
        (PEGI12, 'Pegi-12'),
        (PEGI16, 'Pegi-16'),
        (PEGI18, 'Pegi-18')
    )
    ograniczenia_wiekowe = models.CharField(max_length=200, choices=AGE)
    last_update = models.DateTimeField(auto_now_add=True)
    jezyk_id = models.ForeignKey(Jezyk, on_delete=models.CASCADE)
    ocena = models.BooleanField(default=True)

class Gatunek(models.Model):
    nazwa = models.CharField(max_length=25, blank=False)
    last_update = models.DateTimeField(auto_now_add=True)

class GatunekGry(models.Model):
    gra_id = models.ForeignKey(Gra, on_delete=models.CASCADE)
    gatunek_id = models.ForeignKey(Gatunek, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now_add=True)

class SklepGier(models.Model):
    gra_id = models.ForeignKey(Gra, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now_add=True)

class GraText(models.Model):
    gra_id = models.ForeignKey(Gra, on_delete=models.CASCADE)
    tytul = models.CharField(max_length=255, blank=False)
    opis = models.TextField()

class Biblioteka(models.Model):
    gra_id = models.ForeignKey(Gra, on_delete=models.CASCADE)
    status_instalacji = models.BooleanField(default=False)
    wartosc = models.DecimalField(max_digits=6, decimal_places=2)

class Adres(models.Model):
    panstwo = models.CharField(max_length=50, blank=False)
    last_update = models.DateTimeField(auto_now_add=True)

class Uzytkownik(models.Model):
    imie = models.CharField(max_length=45, blank=False)
    last_name = models.CharField(max_length=45, blank=False)
    email = models.CharField(max_length=50, blank=False)
    adres_id = models.ForeignKey(Adres, on_delete=models.CASCADE)
    aktywny = models.BooleanField(default=False)
    data_utworzenia_konta = models.DateField()
    last_update = models.DateTimeField(auto_now_add=True)
    biblioteka_id = models.ForeignKey(Biblioteka, on_delete=models.CASCADE)

class Zakup(models.Model):
    data_zakupu = models.DateField()
    sklep_gier_id = models.ForeignKey(SklepGier, on_delete=models.CASCADE)
    uzytkownik_id = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE)
    return_date = models.DateField()
    last_update = models.DateTimeField(auto_now_add=True)

class Platnosc(models.Model):
    uzytkownik_id = models.ForeignKey(Uzytkownik, on_delete=models.CASCADE)
    cena = models.DecimalField(max_digits=5, decimal_places=2)
    data_platnosci = models.DateField()
    last_update = models.DateTimeField(auto_now_add=True)
