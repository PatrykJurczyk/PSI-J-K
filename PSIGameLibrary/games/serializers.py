from rest_framework import serializers
from .models import Uzytkownik, Producent, Gatunek, Gra
from datetime import date

class UzytkownikSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(required=True, max_length = 45)
    nazwisko = serializers.CharField(required=True, max_length=45)
    email = serializers.CharField(required=True, max_length=50)
    aktywny = serializers.BooleanField(required=True)

    def create(self, validated_data):
        return Uzytkownik.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.email = validated_data.get('email', instance.email)
        instance.aktywny = validated_data.get('aktywny', instance.aktywny)
        instance.save()
        return instance

class ProducentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nazwa = serializers.CharField(required=True, max_length = 45)
    rok_zalozenia = serializers.DateField()
    siedziba = serializers.CharField(required = True, max_length=45)
    ilosc_czlonkow = serializers.IntegerField(required=True)

    def date_validation(self,data):
        if data['rok_zalozenia'] > date.today():
            raise serializers.ValidationError("data założenia nie może być późniejsza niż dzień dzisiejszy")

    def create(self, validated_data):
        return Producent.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.rok_zalozenia = validated_data.get('rok_zalozenia', instance.rok_zalozenia)
        instance.siedziba = validated_data.get('siedziba', instance.siedziba)
        instance.ilosc_czlonkow = validated_data.get('ilosc_czlonkow', instance.ilosc_czlonkow)
        instance.save()
        return instance


class GatunekSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nazwa = serializers.CharField(required=True, max_length=45)

    def create(self, validated_data):
        return Gatunek.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.save()
        return instance

class GraSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    tytul = serializers.CharField(required=True, max_length=20)
    opis = serializers.CharField( required=True, max_length=20)
    pegi = serializers.CharField(required=True, max_length=20)
    ocena = serializers.CharField(required=True, max_length=20)
    rok_produkcji = serializers.DateField()
    idUzytkownika = serializers.CharField(required=True, max_length=40)
    idGatunku = serializers.CharField(required=True, max_length=40)
    idProducenta = serializers.CharField(required=True, max_length=40)

    def create(self, validated_data):
        return Gra.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.tytul = validated_data.get('tytul', instance.tytul)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.pegi = validated_data.get('pegi', instance.pegi)
        instance.ocena = validated_data.get('ocena', instance.ocena)
        instance.rok_produkcji = validated_data.get('rok_produkcji', instance.rok_produkcji)
        instance.idUzytkownika = validated_data.get('idUzytkownika', instance.Uzytkownik)
        instance.save()
        return instance
