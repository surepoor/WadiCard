from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
	heros = Hero.objects.all()
	data = {
		'heros': heros,
	}
	return render(request, 'home.html', data)

def company(request):
	return render(request, 'indexcompany.html')