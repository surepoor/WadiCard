# Generated by Django 3.2.9 on 2022-02-16 11:35

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_ad', models.ImageField(upload_to='photos/ad')),
                ('link', models.URLField(max_length=150)),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('end_date', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_com', models.ImageField(upload_to='photos/company')),
                ('name_com', models.CharField(max_length=50)),
                ('category_com', models.CharField(choices=[('الإعلام', 'الإعلام'), ('الطوارئ', 'الطوارئ'), ('القطاع الحكومي', 'القطاع الحكومي'), ('الصحة', 'الصحة'), ('خدمات الإعاشة ', 'خدمات الإعاشة'), ('التجزئة', 'التجزئة'), ('الإتصالات', 'الإتصالات'), ('الطيران', 'الطيران'), ('السكن', 'السكن'), ('المواصلات', 'المواصلات'), ('الإلكترونيات', 'الإلكترونيات'), ('البنوك', 'البنوك'), ('التعليم', 'التعليم'), ('الطوافة', 'الطوافة'), ('الأمن والسلامة', 'الأمن والسلامة')], default='none', max_length=50)),
                ('slug_com', models.CharField(choices=[('media', 'الاعلام'), ('emergency', 'الطوارئ'), ('governance', 'القطاع الحكومي'), ('health', 'الصحة'), ('catering ', 'خدمات الإعاشة'), ('retail', 'التجزئة'), ('telecom', 'الإتصالات'), ('aviation', 'الطيران'), ('living', 'السكن'), ('transportation', 'المواصلات'), ('electronics', 'الإلكترونيات'), ('banks', 'البنوك'), ('education', 'التعليم'), ('twafah', 'الطوافة'), ('safety', 'الأمن والسلامة')], default='none', max_length=50)),
                ('is_special', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('description_com', models.CharField(blank=True, max_length=150)),
                ('location', models.CharField(blank=True, max_length=70)),
                ('city', models.CharField(choices=[('مكة', 'مكة'), ('الرياض', 'الرياض'), ('جدة', 'جدة'), ('المدينة المنورة', 'المدينة المنورة'), ('الدمام', 'الدمام'), ('الطائف', 'الطائف'), ('حائل', 'حائل'), ('ينبع', 'ينبع')], max_length=70)),
                ('phone_num', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('website', models.URLField(blank=True, max_length=150)),
                ('facebook_link', models.URLField(blank=True, max_length=100)),
                ('twitter_link', models.URLField(blank=True, max_length=100)),
                ('instgram_link', models.URLField(blank=True, max_length=100)),
                ('linkedin_link', models.URLField(blank=True, max_length=100)),
                ('whatsapp_link', models.URLField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('end_date', models.DateTimeField(blank=True)),
            ],
        ),
    ]
