from django.db import models
from django.db.models.expressions import Case
from django.db.models.deletion import CASCADE
from django.db.models.fields import Field
import django.utils.timezone as timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager, User

class UserAccountManager(BaseUserManager):
    def create_user(self, firstname, lastname, email, phone, password=None):
        email=self.normalize_email(email)
        user=self.model(email=email, firstname=firstname, lastname=lastname, phone=phone)

        user.set_password(password)
        
        user.save()
        return user
    def create_superuser(self, firstname, lastname, email, phone, password=None):
        user=self.model(email=email, firstname=firstname, lastname=lastname, phone=phone)
        is_active=True
        user.set_password(password)
        user.save()
        is_staff = True
        return user

class Users(AbstractBaseUser, PermissionsMixin):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email = models.EmailField(max_length=40, unique=True)
    phone =models.CharField(max_length=20, unique=True)
    is_active=models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects=UserAccountManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['firstname','lastname','password']

    def __str__(self):
        return self.email