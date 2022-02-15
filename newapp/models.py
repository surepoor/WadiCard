from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.core.validators import FileExtensionValidator




# Create your models here.
class Hero(models.Model):
	join_us = models.URLField(max_length=150)



# class Category(models.Model):
# 	logo_cat = models.ImageField(upload_to='photos/category')
# 	name_cat = models.CharField(max_length=50)
# 	slug_cat = models.CharField(max_length=50, default='none')
# 	desc_cat = models.CharField(max_length=150)
# 	date_created = models.DateTimeField(default=datetime.now, blank=True)


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

	slug_choices = (
		('media', 'الاعلام'),
		('emergency', 'الطوارئ'),
		('governance', 'القطاع الحكومي'),
		('health', 'الصحة'),
		('catering ', 'خدمات الإعاشة'),
		('retail', 'التجزئة'),
		('telecom', 'الإتصالات'),
		('aviation', 'الطيران'),
		('living', 'السكن'),
		('transportation', 'المواصلات'),
		('electronics', 'الإلكترونيات'),
		('banks', 'البنوك'),

	)

	logo_com = models.ImageField(upload_to='photos/company')
	name_com = models.CharField(max_length=50)
	slug_com = models.CharField(max_length=50, choices=slug_choices, default='none')
	is_featured = models.BooleanField(default=False)
	desc_com = models.CharField(max_length=150, blank=True)
	location = models.CharField(max_length=70, blank=True)
	city = models.CharField(max_length=70, choices= city_choices)
	phone = models.IntegerField()
	website = models.URLField(max_length=150, blank=True)
	facebook_link = models.URLField(max_length=100, blank=True)
	twitter_link = models.URLField(max_length=100, blank=True)
	instgram_link = models.URLField(max_length=100, blank=True)
	linkedin_link = models.URLField(max_length=100, blank=True)
	whatsapp_link = models.URLField(max_length=100, blank=True)
	email = models.EmailField(max_length=255, blank=True)
	date_created = models.DateTimeField(default=datetime.now, blank=True)
	end_date = models.DateTimeField(blank=True)

class Ad(models.Model):
	image_ad = models.ImageField(upload_to='photos/ad')
	link = models.URLField(max_length=150)
	date_created = models.DateTimeField(default=datetime.now, blank=True)
	end_date = models.DateTimeField(blank=True)


