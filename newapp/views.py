from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
	heros = Hero.objects.all()
	categorys = Category.objects.all()
	companys = Company.objects.all()
	data = {
		'heros': heros,
		'categorys':categorys,
		'companys':companys,

	}
	return render(request, 'home.html', data)

def company(request):
	companys = Company.objects.all()
	data = {
		'companys': companys,

	}
	return render(request, 'indexcompany.html', data)

def details(request, name_cat):
	return render(request, 'indextest.html')