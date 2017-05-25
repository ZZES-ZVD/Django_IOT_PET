from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()

class Message(models.Model):
    title = models.CharField(max_length=30)
    textarea = models.CharField(max_length=50)
    people = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)

class Status(models.Model):
    num = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

class Iotdata(models.Model):
    tem = models.IntegerField()
    hum = models.IntegerField()
    door = models.IntegerField()
    feng = models.IntegerField()
    indoor = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)