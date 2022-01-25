from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from .models import Gra
from .serializers import GraSerializer
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
