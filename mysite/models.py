from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

class Iotdata(models.Model):
    tem = models.IntegerField(max_length=50)
    hum = models.IntegerField(max_length=50)
    door = models.IntegerField(max_length=10)
    feng = models.IntegerField(max_length=10)
    indoor = models.IntegerField(max_length=10)
    time = models.CharField(max_length=50)