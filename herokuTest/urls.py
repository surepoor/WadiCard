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
from django.contrib.staticfiles.storage import staticfiles_storage
from newapp.views import *
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap
from newapp.sitemaps import *

sitemaps = {
    'static': StaticViewSitemap,

}



urlpatterns = [
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/assets/img/favicon.ico')),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('assets/img/favicon.ico'))),
    # path('Sh_log', admin.site.urls),
    path('admin', admin.site.urls),
    # path('', home, name='home'),
    # path('company', company, name='company'),
    # path('search', search, name='search'),
    # path('about', about, name='about'),
    # path('register', register, name='register'),
    path('', carddunia, name='carddunia'),
    path('cardppmdc', cardppmdc, name='cardppmdc'),
    # path('map', mapage, name='map'),
    # path('success', success, name='success'),
    # path('<slug:slug_com>', details, name='details'),
    # path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
    # re_path(r'^photos/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    # re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'newapp.views.view_404'