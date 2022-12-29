from django.shortcuts import render
from .models import Users, Training
from .serializers import UserCreateSerial, TrainingSerial
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
import requests
login = ""
def getcookie(request):
    global login
    login = request.COOKIES.get('login')
    return HttpResponse(login)
    
class TrainingView(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerial