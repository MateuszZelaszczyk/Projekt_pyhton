from rest_framework import serializers
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from .models import Training, Users

User=get_user_model()

class UserCreateSerial(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model=User
        fields=('id','firstname','lastname','email','password')

class TrainingSerial(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields ="__all__"


class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields ="__all__"
