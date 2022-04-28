from django.shortcuts import render, get_list_or_404, redirect
from .models import *
from django.http import HttpResponse

from django.db.models import Q
from functools import reduce
from operator import or_
# import cloudinary
# import cloudinary.uploader
# import cloudinary.api
from random import shuffle
from PIL import Image, ImageFont, ImageDraw
import cloudinary

# Create your views here.
def home(request):
	# heros = Hero.objects.all()
	ads = Ad.objects.order_by('-date_created')
	# companys = Company.objects.order_by('date_created')
	companys = list(Company.objects.all())  # convert here queryset to list
	shuffle(companys)

	data = {
		# 'heros': heros,
		'companys': companys,
		'ads': ads,

	}
	return render(request, 'home.html', data)

def company(request):
	# companys = Company.objects.all()
	companys = list(Company.objects.all())  # convert here queryset to list
	shuffle(companys)

	data = {
		# 'heros': heros,
		'companys': companys,

	}
	return render(request, 'indexcompany.html', data)

def about(request):
	return render(request, 'about-us.html')

def details(request, slug_com):
	all_cats = get_list_or_404(Company, slug_com=slug_com)
	shuffle(all_cats)
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
		name_com = request.POST['name_com']
		category_com = request.POST['category_com']
		description_com = request.POST['description_com']
		city = request.POST['city']
		location = request.POST['location']
		website = request.POST['website']
		facebook_link = request.POST['facebook_link']
		twitter_link = request.POST['twitter_link']
		instgram_link = request.POST['instgram_link']
		linkedin_link = request.POST['linkedin_link']
		whatsapp_link = request.POST['whatsapp_link']
		email = request.POST['email']

		if Register.objects.filter(name_com=name_com).exists():
			return redirect('register')

		else:
			register = Register.objects.create(name_com=name_com, category_com=category_com,
											   description_com=description_com,
											   city=city, location=location, website=website,
											   facebook_link=facebook_link, twitter_link=twitter_link,
											   instgram_link=instgram_link, linkedin_link=linkedin_link,
											   whatsapp_link=whatsapp_link, email=email)
			return redirect('success')

	else:
		return render(request, 'register.html')



def mapage(request):
	return render(request, 'map.html')


def success(request):
	return render(request, 'success.html')


def view_404(request, exception=None):
    # make a redirect to homepage
    # you can use the name of url or just the plain link
    return redirect('home') # or redirect('name-of-index-url')




def card(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("card.png")
		title = name_com
		image_edit = ImageDraw.Draw(my_image)


		if 5 <= len(name_com) <= 10:
			image_edit.text((220, 637), title, (130, 130, 131), font=title_font)

		if 11 <= len(name_com) <= 14:
			image_edit.text((205, 637), title, (130, 130, 131), font=title_font)

		elif 15 <= len(name_com) <= 20:
			image_edit.text((175, 637), title, (130, 130, 131), font=title_font)

		elif 21 <= len(name_com) <= 26:
			image_edit.text((150, 637), title, (130, 130, 131), font=title_font)

		# else:
		# 	image_edit.text((180, 637), title, (130, 130, 131), font=title_font)


		# elif len(name_com) > 26:
		# 	image_edit.text((130, 637), title, (130, 130, 131), font=title_font)

		my_image.save("newcard.png")
		image = "newcard.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/card",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'card.html')


