from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import *



class StaticViewSitemap(Sitemap):
	changefreq = 'weekly'
	protocol = 'https'
	priority = 0.8

	def items(self):
		return ['home', 'company', 'about', 'map', 'register']

	def location(self, item):
		return reverse(item)
