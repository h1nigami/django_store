from django.db import models
from django.forms import Widget
from django import forms

class Phone(models.Model):
    name = models.CharField(max_length=255)
    screen = models.CharField(max_length=255)
    memory = models.CharField(max_length=255)
    camera = models.CharField(max_length=255)
    accumulator = models.CharField(max_length=255)
    cpu = models.CharField(max_length=255)
    price = models.IntegerField()
    img = models.ImageField(upload_to='static/img/')   
    def __str__(self) -> str:
        return self.name

class Tarifs(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    description1 = models.CharField(max_length=255)
    price = models.IntegerField()
      
    def __str__(self) -> str:
        return self.name

class Rewiev(models.Model):
    name = models.CharField(max_length=128)
    review = models.TextField()