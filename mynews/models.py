from django.db import models
from django.utils import timezone


class sports(models.Model):
    headline=models.CharField(max_length=20,null=True)
    caption=models.TextField(max_length=50,null=True)
    date_created = models.DateTimeField(default=timezone.now)

class loveDating(models.Model):
    headline=models.CharField(max_length=20,null=True)
    caption=models.TextField(max_length=50,null=True)
    date_created = models.DateTimeField(default=timezone.now)

class EntertainmentMedia(models.Model):
    headline=models.CharField(max_length=20,null=True)
    caption=models.TextField(max_length=50,null=True)
    date_created = models.DateTimeField(default=timezone.now)   

class TravelLeisure(models.Model):
    headline=models.CharField(max_length=20,null=True)
    caption=models.TextField(max_length=50,null=True)
    date_created = models.DateTimeField(default=timezone.now)






