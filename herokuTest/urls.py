"""herokuTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

from newapp.views import *

urlpatterns = [
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico')),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('company', company, name='company'),
    path('search', search, name='search'),
    path('about', about, name='about'),
    path('register', register, name='register'),
    path('<slug:slug_com>', details, name='details'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
