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



size1 = 240
size2 = 637
size3 = 230
size4 = 637
size5 = 200
size6 = 637
size7 = 190
size8 = 637



def carddunia(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("dunia.jpeg")
		title = name_com
		image_edit = ImageDraw.Draw(my_image)


		if 5 <= len(name_com) <= 10:
			image_edit.text((size1, size2), title, (130, 130, 131), font=title_font)

		if 11 <= len(name_com) <= 14:
			image_edit.text((size3, size4), title, (130, 130, 131), font=title_font)

		elif 15 <= len(name_com) <= 20:
			image_edit.text((size5, size6), title, (130, 130, 131), font=title_font)

		elif 21 <= len(name_com) <= 26:
			image_edit.text((size7, size8), title, (130, 130, 131), font=title_font)

		# else:
		# 	image_edit.text((180, 637), title, (130, 130, 131), font=title_font)


		# elif len(name_com) > 26:
		# 	image_edit.text((130, 637), title, (130, 130, 131), font=title_font)

		my_image.save("dunia.png")
		image = "dunia.png"
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
		return render(request, 'temp/card.html')


def cardppmdc(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("ppmdc.jpeg")
		title = name_com
		image_edit = ImageDraw.Draw(my_image)


		if 5 <= len(name_com) <= 10:
			image_edit.text((size1, size2), title, (130, 130, 131), font=title_font)

		if 11 <= len(name_com) <= 14:
			image_edit.text((size3, size4), title, (130, 130, 131), font=title_font)

		elif 15 <= len(name_com) <= 20:
			image_edit.text((size5, size6), title, (130, 130, 131), font=title_font)

		elif 21 <= len(name_com) <= 26:
			image_edit.text((size7, size8), title, (130, 130, 131), font=title_font)

		# else:
		# 	image_edit.text((180, 637), title, (130, 130, 131), font=title_font)


		# elif len(name_com) > 26:
		# 	image_edit.text((130, 637), title, (130, 130, 131), font=title_font)

		my_image.save("ppmdc.png")
		image = "ppmdc.png"
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
		return render(request, 'temp/cardppmdc.html')


def cardbinladen(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/binladin.jpeg")
		title = name_com
		image_edit = ImageDraw.Draw(my_image)


		if 5 <= len(name_com) <= 10:
			image_edit.text((size1, size2), title, (130, 130, 131), font=title_font)

		if 11 <= len(name_com) <= 14:
			image_edit.text((size3, size4), title, (130, 130, 131), font=title_font)

		elif 15 <= len(name_com) <= 20:
			image_edit.text((size5, size6), title, (130, 130, 131), font=title_font)

		elif 21 <= len(name_com) <= 26:
			image_edit.text((size7, size8), title, (130, 130, 131), font=title_font)

		# else:
		# 	image_edit.text((180, 637), title, (130, 130, 131), font=title_font)


		# elif len(name_com) > 26:
		# 	image_edit.text((130, 637), title, (130, 130, 131), font=title_font)

		my_image.save("photos/binladin.png")
		image = "photos/binladin.png"
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
		return render(request, 'temp/cardbinladin.html')


def cardwatan(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/watan.jpeg")
		title = name_com
		image_edit = ImageDraw.Draw(my_image)


		if 5 <= len(name_com) <= 10:
			image_edit.text((size1, size2), title, (130, 130, 131), font=title_font)

		if 11 <= len(name_com) <= 14:
			image_edit.text((size3, size4), title, (130, 130, 131), font=title_font)

		elif 15 <= len(name_com) <= 20:
			image_edit.text((size5, size6), title, (130, 130, 131), font=title_font)

		elif 21 <= len(name_com) <= 26:
			image_edit.text((size7, size8), title, (130, 130, 131), font=title_font)

		# else:
		# 	image_edit.text((180, 637), title, (130, 130, 131), font=title_font)


		# elif len(name_com) > 26:
		# 	image_edit.text((130, 637), title, (130, 130, 131), font=title_font)

		my_image.save("photos/watan.png")
		image = "photos/watan.png"
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
		return render(request, 'temp/cardwatan.html')


def cardcpc(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/cpc.jpeg")
		title = name_com
		image_edit = ImageDraw.Draw(my_image)


		if 5 <= len(name_com) <= 10:
			image_edit.text((size1, size2), title, (130, 130, 131), font=title_font)

		if 11 <= len(name_com) <= 14:
			image_edit.text((size3, size4), title, (130, 130, 131), font=title_font)

		elif 15 <= len(name_com) <= 20:
			image_edit.text((size5, size6), title, (130, 130, 131), font=title_font)

		elif 21 <= len(name_com) <= 26:
			image_edit.text((size7, size8), title, (130, 130, 131), font=title_font)

		# else:
		# 	image_edit.text((180, 637), title, (130, 130, 131), font=title_font)


		# elif len(name_com) > 26:
		# 	image_edit.text((130, 637), title, (130, 130, 131), font=title_font)

		my_image.save("photos/cpc.png")
		image = "photos/cpc.png"
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
		return render(request, 'temp/cardcpc.html')




def cardpremco(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/premco.jpeg")
		title = name_com
		image_edit = ImageDraw.Draw(my_image)


		if 5 <= len(name_com) <= 10:
			image_edit.text((size1, size2), title, (130, 130, 131), font=title_font)

		if 11 <= len(name_com) <= 14:
			image_edit.text((size3, size4), title, (130, 130, 131), font=title_font)

		elif 15 <= len(name_com) <= 20:
			image_edit.text((size5, size6), title, (130, 130, 131), font=title_font)

		elif 21 <= len(name_com) <= 26:
			image_edit.text((size7, size8), title, (130, 130, 131), font=title_font)

		# else:
		# 	image_edit.text((180, 637), title, (130, 130, 131), font=title_font)


		# elif len(name_com) > 26:
		# 	image_edit.text((130, 637), title, (130, 130, 131), font=title_font)

		my_image.save("photos/premco.png")
		image = "photos/premco.png"
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
		return render(request, 'temp/cardpremco.html')


def carduaac(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/UAAC.jpeg")
		title = name_com
		image_edit = ImageDraw.Draw(my_image)


		if 5 <= len(name_com) <= 10:
			image_edit.text((size1, size2), title, (130, 130, 131), font=title_font)

		if 11 <= len(name_com) <= 14:
			image_edit.text((size3, size4), title, (130, 130, 131), font=title_font)

		elif 15 <= len(name_com) <= 20:
			image_edit.text((size5, size6), title, (130, 130, 131), font=title_font)

		elif 21 <= len(name_com) <= 26:
			image_edit.text((size7, size8), title, (130, 130, 131), font=title_font)

		# else:
		# 	image_edit.text((180, 637), title, (130, 130, 131), font=title_font)


		# elif len(name_com) > 26:
		# 	image_edit.text((130, 637), title, (130, 130, 131), font=title_font)

		my_image.save("photos/uaac.png")
		image = "photos/uaac.png"
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
		return render(request, 'temp/carduaac.html')


def cardmgic(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/mgic.jpeg")
		title = name_com
		image_edit = ImageDraw.Draw(my_image)


		if 5 <= len(name_com) <= 10:
			image_edit.text((size1, size2), title, (130, 130, 131), font=title_font)

		if 11 <= len(name_com) <= 14:
			image_edit.text((size3, size4), title, (130, 130, 131), font=title_font)

		elif 15 <= len(name_com) <= 20:
			image_edit.text((size5, size6), title, (130, 130, 131), font=title_font)

		elif 21 <= len(name_com) <= 26:
			image_edit.text((size7, size8), title, (130, 130, 131), font=title_font)

		# else:
		# 	image_edit.text((180, 637), title, (130, 130, 131), font=title_font)


		# elif len(name_com) > 26:
		# 	image_edit.text((130, 637), title, (130, 130, 131), font=title_font)

		my_image.save("photos/mgic.png")
		image = "photos/mgic.png"
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
		return render(request, 'temp/cardmgic.html')


def cardtower(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/tower.jpeg")
		title = name_com
		image_edit = ImageDraw.Draw(my_image)


		if 5 <= len(name_com) <= 10:
			image_edit.text((size1, size2), title, (130, 130, 131), font=title_font)

		if 11 <= len(name_com) <= 14:
			image_edit.text((size3, size4), title, (130, 130, 131), font=title_font)

		elif 15 <= len(name_com) <= 20:
			image_edit.text((size5, size6), title, (130, 130, 131), font=title_font)

		elif 21 <= len(name_com) <= 26:
			image_edit.text((size7, size8), title, (130, 130, 131), font=title_font)

		# else:
		# 	image_edit.text((180, 637), title, (130, 130, 131), font=title_font)


		# elif len(name_com) > 26:
		# 	image_edit.text((130, 637), title, (130, 130, 131), font=title_font)

		my_image.save("photos/tower.png")
		image = "photos/tower.png"
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
		return render(request, 'temp/cardmgic.html')


def cardtower(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/tower.jpeg")
		title = name_com
		image_edit = ImageDraw.Draw(my_image)


		if 5 <= len(name_com) <= 10:
			image_edit.text((size1, size2), title, (130, 130, 131), font=title_font)

		if 11 <= len(name_com) <= 14:
			image_edit.text((size3, size4), title, (130, 130, 131), font=title_font)

		elif 15 <= len(name_com) <= 20:
			image_edit.text((size5, size6), title, (130, 130, 131), font=title_font)

		elif 21 <= len(name_com) <= 26:
			image_edit.text((size7, size8), title, (130, 130, 131), font=title_font)

		# else:
		# 	image_edit.text((180, 637), title, (130, 130, 131), font=title_font)


		# elif len(name_com) > 26:
		# 	image_edit.text((130, 637), title, (130, 130, 131), font=title_font)

		my_image.save("photos/tower.png")
		image = "photos/tower.png"
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
		return render(request, 'temp/cardmgic.html')


def cardempower(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/empower.jpeg")
		title = name_com
		image_edit = ImageDraw.Draw(my_image)


		if 5 <= len(name_com) <= 10:
			image_edit.text((size1, size2), title, (130, 130, 131), font=title_font)

		if 11 <= len(name_com) <= 14:
			image_edit.text((size3, size4), title, (130, 130, 131), font=title_font)

		elif 15 <= len(name_com) <= 20:
			image_edit.text((size5, size6), title, (130, 130, 131), font=title_font)

		elif 21 <= len(name_com) <= 26:
			image_edit.text((size7, size8), title, (130, 130, 131), font=title_font)

		# else:
		# 	image_edit.text((180, 637), title, (130, 130, 131), font=title_font)


		# elif len(name_com) > 26:
		# 	image_edit.text((130, 637), title, (130, 130, 131), font=title_font)

		my_image.save("photos/empower.png")
		image = "photos/empower.png"
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
		return render(request, 'temp/cardempower.html')


def cardbsc(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/BSC.jpeg")
		title = name_com
		image_edit = ImageDraw.Draw(my_image)


		if 5 <= len(name_com) <= 10:
			image_edit.text((size1, size2), title, (130, 130, 131), font=title_font)

		if 11 <= len(name_com) <= 14:
			image_edit.text((size3, size4), title, (130, 130, 131), font=title_font)

		elif 15 <= len(name_com) <= 20:
			image_edit.text((size5, size6), title, (130, 130, 131), font=title_font)

		elif 21 <= len(name_com) <= 26:
			image_edit.text((size7, size8), title, (130, 130, 131), font=title_font)

		# else:
		# 	image_edit.text((180, 637), title, (130, 130, 131), font=title_font)


		# elif len(name_com) > 26:
		# 	image_edit.text((130, 637), title, (130, 130, 131), font=title_font)

		my_image.save("photos/BSC.png")
		image = "photos/BSC.png"
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
		return render(request, 'temp/cardempower.html')