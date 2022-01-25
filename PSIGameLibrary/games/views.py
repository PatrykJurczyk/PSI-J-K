from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from .models import Gra, Gatunek, Uzytkownik, Producent
from .serializers import GraSerializer, GatunekSerializer, UzytkownikSerializer, ProducentSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def games_list(request):
    if request.method == 'GET':
        gra = Gra.objects.all()
        serializer = GraSerializer(gra, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def genre_list(request):
    if request.method == 'GET':
        gatunek = Gatunek.objects.all()
        serializer = GatunekSerializer(gatunek, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = GatunekSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        uzytkownik = Uzytkownik.objects.all()
        serializer = UzytkownikSerializer(uzytkownik, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UzytkownikSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def producer_list(request):
    if request.method == 'GET':
        producent = Producent.objects.all()
        serializer = ProducentSerializer(producent, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProducentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)