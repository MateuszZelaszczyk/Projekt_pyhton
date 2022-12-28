from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from .models import Training

User=get_user_model()

class UserCreateSerial(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=User
        fields=('id','firstname','lastname','email','password')

class TrainingSerial(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields ="__all__"