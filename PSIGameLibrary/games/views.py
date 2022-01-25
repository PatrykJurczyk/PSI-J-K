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
