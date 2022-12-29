from django.db import models
from django.db.models.expressions import Case
from django.db.models.deletion import CASCADE
from django.db.models.fields import Field
import django.utils.timezone as timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager, User
import  datetime

class UserAccountManager(BaseUserManager):
    def create_user(self, firstname, lastname, email, password=None):
        email=self.normalize_email(email)
        user=self.model(email=email, firstname=firstname, lastname=lastname)

        user.set_password(password)
        
        user.save()
        return user
    def create_superuser(self, firstname, lastname, email, password=None):
        user=self.model(email=email, firstname=firstname, lastname=lastname)
        is_active=True
        user.set_password(password)
        user.save()
        is_staff = True
        return user

class Users(AbstractBaseUser, PermissionsMixin):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email = models.EmailField(max_length=40, unique=True)
    is_active=models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects=UserAccountManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['firstname','lastname','password']

    def __str__(self):
        return self.email

class Training(models.Model):
    email=models.EmailField()
    dyscyplina=models.CharField(max_length=50)
    nazwa=models.CharField(max_length=50)
    dystans=models.FloatField(default=0)
    czas= models.TimeField(default=0)
    sredne_tempo = models.CharField(max_length=50, default="")
    srednia_predkosc = models.FloatField(default=0)
    data = models.DateField(default=datetime.date.today)
    def save(self,*args,**kwargs):
        time_conv = float(self.czas.strftime('%H'))+(float(self.czas.strftime('%M'))/60)+(float(self.czas.strftime('%S'))/3600)
        self.srednia_predkosc=self.dystans/time_conv
        self.srednia_predkosc=round(self.srednia_predkosc,2)
        
        time_conv2 = (float(self.czas.strftime('%H'))*60)+float(self.czas.strftime('%M'))+(float(self.czas.strftime('%S'))/60)
        self.sredne_tempo = ((time_conv2/self.dystans))
        dziesietna= self.sredne_tempo-int(self.sredne_tempo)
        if dziesietna*0.6<0.1:
            self.sredne_tempo=(str(int(self.sredne_tempo))+":0"+str(round((dziesietna*0.6)*100)))
        else:
            self.sredne_tempo=(str(int(self.sredne_tempo))+":"+str(round((dziesietna*0.6)*100)))

        super(Training, self).save(*args, **kwargs)
    def __str__(self):
        return self.nazwa