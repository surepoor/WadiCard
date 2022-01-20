from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html')

def company(request):
	return render(request, 'index-company.html')