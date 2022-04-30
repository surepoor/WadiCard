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
size3 = 215
size31 = 220
size4 = 637
size5 = 200
size51 = 190
size6 = 637
size7 = 175
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
		return render(request, 'temp/cardtower.html')



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
		return render(request, 'temp/cardbsc.html')


def cardprm(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/prm.jpeg")
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

		my_image.save("photos/prm.png")
		image = "photos/prm.png"
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
		return render(request, 'temp/cardprm.html')


def cardrec(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/rec.jpeg")
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

		my_image.save("photos/rec.png")
		image = "photos/rec.png"
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
		return render(request, 'temp/cardrec.html')


def cardsacodeco(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/sacodeco.jpeg")
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

		my_image.save("photos/sacodeco.png")
		image = "photos/sacodeco.png"
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
		return render(request, 'temp/cardsacodeco.html')


def cardbtat(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/btat.jpeg")
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

		my_image.save("photos/btat.png")
		image = "photos/btat.png"
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
		return render(request, 'temp/cardbtat.html')


def cardbtgroup(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/btgroup.jpeg")
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

		my_image.save("photos/btgroup.png")
		image = "photos/btgroup.png"
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
		return render(request, 'temp/cardbtgroup.html')


def cardhasoub(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/hasoub.jpeg")
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

		my_image.save("photos/hasoub.png")
		image = "photos/hasoub.png"
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
		return render(request, 'temp/cardhasoub.html')


def cardhsb(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/hsb.jpeg")
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

		my_image.save("photos/hsb.png")
		image = "photos/hsb.png"
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
		return render(request, 'temp/cardhsb.html')


def cardbtam(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/btam.jpeg")
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

		my_image.save("photos/btam.png")
		image = "photos/btam.png"
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
		return render(request, 'temp/cardbtam.html')


def carddsb(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/DSP.jpeg")
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

		my_image.save("photos/DSP.png")
		image = "photos/DSP.png"
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
		return render(request, 'temp/carddsp.html')


def cardmubadra(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/mubadra.jpeg")
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

		my_image.save("photos/mubadra.png")
		image = "photos/mubadra.png"
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
		return render(request, 'temp/cardmubadra.html')



def cardpmdc(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/pmdc.jpeg")
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

		my_image.save("photos/pmdc.png")
		image = "photos/pmdc.png"
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
		return render(request, 'temp/cardpmdc.html')


def cardvddc(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/vddc.jpeg")
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

		my_image.save("photos/vddc.png")
		image = "photos/vddc.png"
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
		return render(request, 'temp/cardvddc.html')


def cardalborg(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/alborg.jpeg")
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

		my_image.save("photos/alborg.png")
		image = "photos/alborg.png"
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
		return render(request, 'temp/cardalborg.html')


def cardabcc(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/abcc.jpeg")
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

		my_image.save("photos/abcc.png")
		image = "photos/abcc.png"
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
		return render(request, 'temp/cardabcc.html')


def cardhdhc(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/hdhc2.jpeg")
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

		my_image.save("photos/hdhc.png")
		image = "photos/hdhc.png"
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
		return render(request, 'temp/cardhdhc.html')


def cardkone(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/kone2.jpeg")
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

		my_image.save("photos/kone.png")
		image = "photos/kone.png"
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
		return render(request, 'temp/cardkone.html')


def cardbihg(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/bihg.jpeg")
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

		my_image.save("photos/bihg.png")
		image = "photos/bihg.png"
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
		return render(request, 'temp/cardbihg.html')


def cardjonson(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/jonson.jpeg")
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

		my_image.save("photos/jonson.png")
		image = "photos/jonson.png"
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
		return render(request, 'temp/cardjonson.html')


def cardbcg(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/bcg.jpg")
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
			folder="/card",
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
		my_image = Image.open("photos/bihgen.jpg")
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

		my_image.save("photos/bihgen.png")
		image = "photos/bihgen.png"
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
		return render(request, 'temp/cardbihgen.html')


def cardwatanen(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('Frutiger LT 45 Light.ttf',24)
		my_image = Image.open("photos/watanen.jpg")
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

		my_image.save("photos/watanen.png")
		image = "photos/watanen.png"
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
		return render(request, 'temp/cardwatanen.html')



def cardfast(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/fast.jpeg")
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

		my_image.save("photos/fast.png")
		image = "photos/fast.png"
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
		return render(request, 'temp/cardfast.html')


def cardpcmc(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/pcmc.jpeg")
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

		my_image.save("photos/pcmc.png")
		image = "photos/pcmc.png"
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
		return render(request, 'temp/cardpcmc.html')


def cardsaudi(request):
	if request.method == 'POST':
		name_com = request.POST['name_com']
		title_font = ImageFont.truetype('BigVesta-Arabic-Regular.ttf',24)
		my_image = Image.open("photos/saudi.jpeg")
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

		my_image.save("photos/saudi.png")
		image = "photos/saudi.png"
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
		return render(request, 'temp/cardsaudi.html')

