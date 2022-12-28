from django.db.models.expressions import Value
from django.db.models.lookups import PatternLookup
from django.shortcuts import render
from rest_framework import response
from .models import Users, Training
from .serializers import UserCreateSerial, TrainingSerial
from rest_framework import viewsets, generics, status
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