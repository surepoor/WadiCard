from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
	hero = Hero.objects.all()
	data = {
		'hero': hero,
	}
	return render(request, 'home.html')

def company(request):
	return render(request, 'indexcompany.html')