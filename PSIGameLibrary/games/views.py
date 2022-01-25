from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import Gra, Gatunek, Uzytkownik, Producent
from .serializers import GraSerializer, GatunekSerializer, UzytkownikSerializer, ProducentSerializer
from rest_framework import status
from rest_framework.views import APIView

class GameList(APIView):
    def get(self, request, format=None):
        gra = Gra.objects.all()
        serializer = GraSerializer(gra, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GameDetails(APIView):
    def get_obiect(self, pk):
        try:
            return Gra.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        gra = self.get_obiect(pk)
        serializer = GraSerializer(gra)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        gra = self.get_obiect(pk)
        serializer = GraSerializer(gra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        gra = self.get_obiect(pk)
        gra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GanreList(APIView):
    def get(self, request, format=None):
        gatunek = Gatunek.objects.all()
        serializer = GatunekSerializer(gatunek, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GatunekSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(APIView):
    def get(self, request, format=None):
        uzytkownik = Uzytkownik.objects.all()
        serializer = UzytkownikSerializer(uzytkownik, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UzytkownikSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProducerList(APIView):
    def get(self, request, format=None):
        producent = Producent.objects.all()
        serializer = ProducentSerializer(producent, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProducentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)