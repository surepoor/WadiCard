from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField




# Create your models here.
class Hero(models.Model):
	image_hero = models.ImageField(upload_to='photos/%y/%m/%d')
	logo_header = models.ImageField(upload_to='photos/%y/%m/%d')
	join_us = models.URLField(max_length=150)



class Category(models.Model):
	logo_cat = models.ImageField(upload_to='photos/category')
	name_cat = models.CharField(max_length=50)
	desc_cat = models.CharField(max_length=150)
	date_created = models.DateTimeField(default=datetime.now(), blank=True)


class Company(models.Model):
	city_choices = (
		('مكة', 'مكة'),
		('الرياض', 'الرياض'),
		('جدة', 'جدة'),
		('المدينة المنورة', 'المدينة المنورة'),
		('الدمام', 'الدمام'),
		('الطائف', 'الطائف'),
		('حائل', 'حائل'),
		('ينبع', 'ينبع'),
	)

	logo_com = models.ImageField(upload_to='photos/company')
	name_com = models.CharField(max_length=50)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	is_featured = models.BooleanField(default=False)
	desc_com = models.CharField(max_length=150)
	location = models.CharField(max_length=70)
	city = MultiSelectField(choices= city_choices)
	phone = models.IntegerField(max_length=15)
	website = models.URLField(max_length=150)
	facebook_link = models.URLField(max_length=100)
	twitter_link = models.URLField(max_length=100)
	instgram_link = models.URLField(max_length=100)
	linkedin_link = models.URLField(max_length=100)
	whatsapp_link = models.URLField(max_length=100)
	email = models.EmailField(max_length=255)
	date_created = models.DateTimeField(default=datetime.now(), blank=True)
	end_date = models.DateTimeField()

class Ad(models.Model):
	image_ad = models.ImageField(upload_to='photos/ad')
	link = models.URLField(max_length=150)
	date_created = models.DateTimeField(default=datetime.now(), blank=True)
	end_date = models.DateTimeField()


