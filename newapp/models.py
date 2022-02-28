from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.core.validators import FileExtensionValidator
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField




# Create your models here.
# class Hero(models.Model):
# 	join_us = models.URLField(max_length=150)



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
		('education', 'التعليم'),
		('twafah', 'الطوافة'),
		('safety', 'الأمن والسلامة'),

	)

	category_choices = (
		('الإعلام', 'الإعلام'),
		('الطوارئ', 'الطوارئ'),
		('القطاع الحكومي', 'القطاع الحكومي'),
		('الصحة', 'الصحة'),
		('خدمات الإعاشة ', 'خدمات الإعاشة'),
		('التجزئة', 'التجزئة'),
		('الإتصالات', 'الإتصالات'),
		('الطيران', 'الطيران'),
		('السكن', 'السكن'),
		('المواصلات', 'المواصلات'),
		('الإلكترونيات', 'الإلكترونيات'),
		('البنوك', 'البنوك'),
		('التعليم', 'التعليم'),
		('الطوافة', 'الطوافة'),
		('الأمن والسلامة', 'الأمن والسلامة'),


	)

	# logo_com = models.ImageField(upload_to='photos/company')
	logo_img = CloudinaryField('logo_img')
	name_com = models.CharField(max_length=50)
	category_com = models.CharField(max_length=50, choices=category_choices, default='none')
	slug_com = models.CharField(max_length=50, choices=slug_choices, default='none')
	is_special = models.BooleanField(default=False)
	is_featured = models.BooleanField(default=False)
	description_com = models.CharField(max_length=170, blank=True)
	location = models.CharField(max_length=70, blank=True)
	city = models.CharField(max_length=70, choices= city_choices)
	# phone = models.IntegerField()
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_num = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
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



class Register(models.Model):

	# logo_com = models.ImageField(upload_to='photos/company')
	name_com = models.CharField(max_length=50)
	category_com = models.CharField(max_length=50, default='none')
	# slug_com = models.CharField(max_length=50, choices=slug_choices, default='none')
	# is_featured = models.BooleanField(default=False)
	description_com = models.CharField(max_length=170, blank=True)
	city = models.CharField(max_length=70,)
	location = models.CharField(max_length=70, blank=True)
	# phone = models.IntegerField()
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_num = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
	website = models.URLField(max_length=150, blank=True)
	facebook_link = models.URLField(max_length=100, blank=True)
	twitter_link = models.URLField(max_length=100, blank=True)
	instgram_link = models.URLField(max_length=100, blank=True)
	linkedin_link = models.URLField(max_length=100, blank=True)
	whatsapp_link = models.URLField(max_length=100, blank=True)
	email = models.EmailField(max_length=255, blank=True)
	review = models.BooleanField(default=False)
	# date_created = models.DateTimeField(default=datetime.now, blank=True)


