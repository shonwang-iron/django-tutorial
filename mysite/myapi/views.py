from django.shortcuts import render
from django.http.response import JsonResponse
# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .serializers import HeroSerializer
from .models import Hero


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

@api_view(['GET', 'POST'])
def fristAPI(request):
    return JsonResponse({'Msg': 'Your use method ' + request.method})

@api_view(['GET', 'POST'])
def getPathParam(request, *args, **kwargs):
    return JsonResponse({'Msg': 'Your request parameter ' + kwargs['name']})