from django.db.models.expressions import Value
from django.db.models.lookups import PatternLookup
from django.shortcuts import render
from rest_framework import response
from .models import Users
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

def getcookie(request):
    global login
    login = request.COOKIES['login']
    return HttpResponse(login)
