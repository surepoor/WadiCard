from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
# admin.site.register(Company)
admin.site.register(Ad)
admin.site.register(Register)

class ComAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 10px;" />'.format(object.logo_img.url))

    thumbnail.short_description = 'Logo'

    list_display = ('id', 'thumbnail', 'name_com', 'city', 'category_com', 'is_special', 'is_featured')

    list_display_links = ('id', 'thumbnail', 'name_com')

    list_editable = ('is_featured', 'is_special')

    search_fields = ('id', 'name_com', 'city', 'description_com','category_com')

    list_filter = ('city', 'name_com', 'category_com', 'is_special', 'is_featured')

admin.site.register(Company, ComAdmin)