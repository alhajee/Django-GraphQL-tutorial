from django.db import models


class Hero(models.Model):
  name = models.CharField(max_length=100)
  gender = models.CharField(max_length=100, choices=(('M', 'Male'), ('F', 'Female')), default='F')
  movie = models.CharField(max_length=100)