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



size1 = 680
size2 = 1100
size3 = 650
size31 = 220
size4 = 1100
size5 = 600
size51 = 190
size6 = 1100
size7 = 600
size8 = 1100

size9 = 400
# sizetestY = 637



def wadi(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('GE-Dinar-One-Bold-1.otf',52)
		my_image = Image.open("photos/wadicard.jpg")
		title = name_com
		image_edit = ImageDraw.Draw(my_image)
		font_color = (95, 95, 95)

		
		
		
		if 4 <= len(name_com) <= 10:
			image_edit.text((size1, size2), title, font_color, font=title_font)

		if 11 <= len(name_com) <= 14:
			image_edit.text((size3, size4), title, font_color, font=title_font)

		elif 15 <= len(name_com) <= 18:
			image_edit.text((size5, size6), title, font_color, font=title_font)

		elif 19 <= len(name_com) <= 21:
			image_edit.text((size7, size8), title, font_color, font=title_font)

		elif 21 <= len(name_com):
			image_edit.text((size9, size8), title, font_color, font=title_font)

		# else:
		# 	image_edit.text((180, 637), title, (130, 130, 131), font=title_font)


		# elif len(name_com) > 26:
		# 	image_edit.text((130, 637), title, (130, 130, 131), font=title_font)

		my_image.save("photos/adhasave/wadiMakkah.png")
		image = "photos/adhasave/wadiMakkah.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="newtest",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/dts7rufgf/image/upload/{}'.format(cloudinary_response))
		print("htmlllll" + html)
		return redirect(html)
	else:
		return render(request, 'temp/card.html')


def carddunia2(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/dunia.jpeg")
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

		my_image.save("photos/adhasave/dunia.png")
		image = "photos/adhasave/dunia.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="testtest",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/dts7rufgf/image/upload/{}'.format(cloudinary_response))
		print("htmlllll" + html)
		return redirect(html)
	else:
		return render(request, 'temp/card.html')


def cardppmdc(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/ppmdc2.jpeg")
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

		my_image.save("photos/adhasave/ppmdc.png")
		image = "photos/adhasave/ppmdc.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/ppmdc",
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
		my_image = Image.open("photos/adha/sbg.jpeg")
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

		my_image.save("photos/adhasave/binladin.png")
		image = "photos/adhasave/binladin.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/binladin",
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
		my_image = Image.open("photos/adha/watan.jpeg")
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

		my_image.save("photos/adhasave/watan.png")
		image = "photos/adhasave/watan.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/watan",
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
		my_image = Image.open("photos/adha/cpc.jpeg")
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

		my_image.save("photos/adhasave/cpc.png")
		image = "photos/adhasave/cpc.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/cpc",
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
		my_image = Image.open("photos/adha/premco.jpeg")
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

		my_image.save("photos/adhasave/premco.png")
		image = "photos/adhasave/premco.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/premco",
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
		my_image = Image.open("photos/adha/uaac.jpeg")
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

		my_image.save("photos/adhasave/uaac.png")
		image = "photos/adhasave/uaac.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/uaac",
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
		my_image = Image.open("photos/adha/mgic.jpeg")
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

		my_image.save("photos/adhasave/mgic.png")
		image = "photos/adhasave/mgic.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/mgic",
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
		my_image = Image.open("photos/adha/towers.jpeg")
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

		my_image.save("photos/adhasave/tower.png")
		image = "photos/adhasave/tower.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/tower",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardtower.html')



def cardempower(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/empower.jpeg")
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

		my_image.save("photos/adhasave/empower.png")
		image = "photos/adhasave/empower.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/empower",
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
		my_image = Image.open("photos/adha/bsc.jpeg")
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

		my_image.save("photos/adhasave/BSC.png")
		image = "photos/adhasave/BSC.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/bsc",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardbsc.html')


def cardprm(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/mix.jpeg")
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

		my_image.save("photos/adhasave/prm.png")
		image = "photos/adhasave/prm.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/prm",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardprm.html')


def cardrec(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/rental.jpeg")
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

		my_image.save("photos/adhasave/rec.png")
		image = "photos/adhasave/rec.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/rec",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardrec.html')


def cardsacodeco(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/sacodeco.jpeg")
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

		my_image.save("photos/adhasave/sacodeco.png")
		image = "photos/adhasave/sacodeco.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/sacodeco",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardsacodeco.html')


def cardbtat(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/btat.jpeg")
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

		my_image.save("photos/adhasave/btat.png")
		image = "photos/adhasave/btat.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/btat",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardbtat.html')


def cardbtgroup(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/btg.jpeg")
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

		my_image.save("photos/adhasave/btgroup.png")
		image = "photos/adhasave/btgroup.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/btgroup",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardbtgroup.html')


def cardhasoub(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/hasoub.jpeg")
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

		my_image.save("photos/adhasave/hasoub.png")
		image = "photos/adhasave/hasoub.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/hasoub",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardhasoub.html')


def cardhsb(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/hsb.jpeg")
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

		my_image.save("photos/adhasave/hsb.png")
		image = "photos/adhasave/hsb.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/hsb",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardhsb.html')


def cardbtam(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/btam.jpeg")
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

		my_image.save("photos/adhasave//btam.png")
		image = "photos/adhasave/btam.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/btam",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardbtam.html')


def carddsb(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/dsp.jpeg")
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

		my_image.save("photos/adhasave/DSP.png")
		image = "photos/adhasave/DSP.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/dsb",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/carddsp.html')


def cardmubadra(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/mubadra.jpeg")
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

		my_image.save("photos/adhasave/mubadra.png")
		image = "photos/adhasave/mubadra.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/mubadra",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardmubadra.html')



def cardpmdc(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/pmdc.jpeg")
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

		my_image.save("photos/adhasave/pmdc.png")
		image = "photos/adhasave/pmdc.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/pmdc",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardpmdc.html')


def cardvddc(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/vision.jpeg")
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

		my_image.save("photos/adhasave/vddc.png")
		image = "photos/adhasave/vddc.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/vddc",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardvddc.html')


def cardalborg(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/")
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

		my_image.save("photos/adhasave/alborg.png")
		image = "photos/adhasave/alborg.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/alborg",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardalborg.html')


def cardabcc(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/arabian.jpeg")
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

		my_image.save("photos/adhasave/abcc.png")
		image = "photos/adhasave/abcc.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/abcc",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardabcc.html')


def cardhdhc(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/hdh.jpeg")
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

		my_image.save("photos/adhasave/hdhc.png")
		image = "photos/adhasave/hdhc.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/hdhc",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardhdhc.html')


def cardkone(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/kone.jpeg")
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

		my_image.save("photos/adhasave/kone.png")
		image = "photos/adhasave/kone.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/kone",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardkone.html')


def cardbihg(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/bihg2.jpeg")
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

		my_image.save("photos/adhasave/bihg.png")
		image = "photos/adhasave/bihg.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/bihg",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardbihg.html')


def cardjonson(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/johnson.jpeg")
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

		my_image.save("photos/adhasave/jonson.png")
		image = "photos/adhasave/jonson.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/jonson",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardjonson.html')


def cardbcg(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/bcg.jpeg")
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

		my_image.save("photos/bcg.png")
		image = "photos/bcg.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/bcg",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardbcg.html')


def cardbihgen(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('Frutiger LT 45 Light.ttf',24)
		my_image = Image.open("photos/adha/bihgen.jpeg")
		title = name_com
		image_edit = ImageDraw.Draw(my_image)


		if 5 <= len(name_com) <= 10:
			image_edit.text((size1, size2), title, (130, 130, 131), font=title_font)

		if 11 <= len(name_com) <= 14:
			image_edit.text((size31, size4), title, (130, 130, 131), font=title_font)

		elif 15 <= len(name_com) <= 20:
			image_edit.text((size5, size6), title, (130, 130, 131), font=title_font)

		elif 21 <= len(name_com) <= 27:
			image_edit.text((size7, size8), title, (130, 130, 131), font=title_font)

		# else:
		# 	image_edit.text((size7, size8), title, (130, 130, 131), font=title_font)


		# elif len(name_com) > 26:
		# 	image_edit.text((130, 637), title, (130, 130, 131), font=title_font)

		my_image.save("photos/adhasave/bihgen.png")
		image = "photos/adhasave/bihgen.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/bihgen",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardbihgen.html')


def cardwatanen(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('Frutiger LT 45 Light.ttf',24)
		my_image = Image.open("photos/adha/watanen.jpeg")
		title = name_com
		image_edit = ImageDraw.Draw(my_image)


		if 5 <= len(name_com) <= 10:
			image_edit.text((size1, size2), title, (130, 130, 131), font=title_font)

		if 11 <= len(name_com) <= 14:
			image_edit.text((size31, size4), title, (130, 130, 131), font=title_font)

		elif 15 <= len(name_com) <= 20:
			image_edit.text((size51, size6), title, (130, 130, 131), font=title_font)

		elif 21 <= len(name_com) <= 27:
			image_edit.text((size7, size8), title, (130, 130, 131), font=title_font)

		# else:
		# 	image_edit.text((size7, size8), title, (130, 130, 131), font=title_font)


		# elif len(name_com) > 26:
		# 	image_edit.text((130, 637), title, (130, 130, 131), font=title_font)

		my_image.save("photos/adhasave/watanen.png")
		image = "photos/adhasave/watanen.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/watanen",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardwatanen.html')



def cardfast(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/fast.jpeg")
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

		my_image.save("photos/adhasave/fast.png")
		image = "photos/adhasave/fast.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/fast",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardfast.html')


def cardpcmc(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/pcmc.jpeg")
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

		my_image.save("photos/adhasave/pcmc.png")
		image = "photos/adhasave/pcmc.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/pcmc",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardpcmc.html')


def cardsaudi(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/saudi.jpeg")
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

		my_image.save("photos/adhasave/saudi.png")
		image = "photos/adhasave/saudi.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/saudi",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardsaudi.html')


def cardsbg(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/sbg2.jpeg")
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

		my_image.save("photos/adhasave/sbg.png")
		image = "photos/adhasave/sbg.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha/sbg",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardsbg.html')


def cardauth(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/authorized.jpeg")
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

		my_image.save("photos/adhasave/authorized.png")
		image = "photos/adhasave/authorized.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardauth.html')



def cardcare(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/care.jpeg")
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

		my_image.save("photos/adhasave/care.png")
		image = "photos/adhasave/care.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardcare.html')


def cardhealth(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/health.jpeg")
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

		my_image.save("photos/adhasave/health.png")
		image = "photos/adhasave/health.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardhealth.html')


def cardmedex(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/adha/medex.jpeg")
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

		my_image.save("photos/adhasave/medex.png")
		image = "photos/adhasave/medex.png"
		# cloudinary.uploader.upload(image)
		cloudinary_response = cloudinary.uploader.upload_resource(
			image,
			use_filename=True,
			folder="/adha",
		)
		# return redirect('success')
		html = ('https://res.cloudinary.com/hgfcbzcmp/image/upload/{}'.format(cloudinary_response))
		return redirect(html)



	else:
		return render(request, 'temp/cardmedex.html')