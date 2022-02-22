from django.shortcuts import render, get_list_or_404, redirect
from .models import *

from django.db.models import Q
from functools import reduce
from operator import or_

# Create your views here.
def home(request):
	# heros = Hero.objects.all()
	companys = Company.objects.all()
	data = {
		# 'heros': heros,
		'companys':companys,

	}
	return render(request, 'home.html', data)

def company(request):
	companys = Company.objects.all()
	data = {
		# 'heros': heros,
		'companys': companys,

	}
	return render(request, 'indexcompany.html', data)

def about(request):
	return render(request, 'about-us.html')

def details(request, slug_com):
	all_cats = get_list_or_404(Company, slug_com=slug_com)

	data = {
		'all_cats': all_cats,
	}

	return render(request, 'indextest.html', data)



def search(request):
	companys = Company.objects.order_by('-date_created')

	if 'keyword' in request.GET:
		keyword = request.GET['keyword']
		if keyword:
			companys = companys.filter(name_com__icontains=keyword) or companys.filter(description_com__icontains=keyword) \
					   or companys.filter(city__icontains=keyword) or companys.filter(category_com=keyword)



	data = {
		'companys': companys,
	}
	return render(request, 'search.html', data)


def register(request):
	if request.method == 'POST':
		print('Submit successfully')
		return redirect('register')

	else:
		return render(request, 'register.html')
