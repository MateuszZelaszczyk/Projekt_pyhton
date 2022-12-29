from django.shortcuts import render
from .models import Users, Training
from .serializers import UserCreateSerial, TrainingSerial
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.db.models import Sum, F
import requests
login = ""
def getcookie(request):
    global login
    login = request.COOKIES['login']
    return HttpResponse(login)
    
class TrainingView(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerial


@api_view(["GET", "POST"])
def Set_data(request):
    if request.method == 'GET':
        my_training = Training.objects.filter(email=login.replace("%40", "@"))
        dystanse = my_training.values("dyscyplina").annotate(dystans_dyscyplina=Sum('dystans')).order_by('dystans_dyscyplina')
        return Response(dystanse)