from django.db import models

# Create your models here.
class Hero(models.Model):
	image_hero = models.ImageField(upload_to='photos/%y/%m/%d')
	logo_header = models.ImageField(upload_to='photos/%y/%m/%d')
	join_us = models.URLField(max_length=150)
