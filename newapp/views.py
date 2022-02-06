from django.shortcuts import render, get_list_or_404
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

def details(request, slug_com):
	all_cats = get_list_or_404(Company, slug_com=slug_com)
	data = {
		'all_cats': all_cats,
	}
	return render(request, 'indextest.html', data)