# Generated by Django 4.0 on 2022-03-15 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_company_youtube_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='category_com',
            field=models.CharField(choices=[('الإعلام', 'الإعلام'), ('الطوارئ', 'الطوارئ'), ('القطاع الحكومي', 'القطاع الحكومي'), ('الصحة', 'الصحة'), ('خدمات الإعاشة ', 'خدمات الإعاشة'), ('التجزئة', 'التجزئة'), ('الإتصالات', 'الإتصالات'), ('الطيران', 'الطيران'), ('الإسكان', 'الإسكان'), ('المواصلات', 'المواصلات'), ('الإلكترونيات', 'الإلكترونيات'), ('البنوك', 'البنوك'), ('التعليم', 'التعليم'), ('الطوافة', 'الطوافة'), ('الأمن والسلامة', 'الأمن والسلامة'), ('الزراعة', 'الزراعة'), ('القطاع الثالث', 'القطاع الثالث'), ('الاستشارات', 'الاستشارات'), ('القطاع الخاص', 'القطاع الخاص')], default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='slug_com',
            field=models.CharField(choices=[('media', 'الاعلام'), ('emergency', 'الطوارئ'), ('governance', 'القطاع الحكومي'), ('health', 'الصحة'), ('catering ', 'خدمات الإعاشة'), ('retail', 'التجزئة'), ('telecom', 'الإتصالات'), ('aviation', 'الطيران'), ('living', 'الإسكان'), ('transportation', 'المواصلات'), ('electronics', 'الإلكترونيات'), ('banks', 'البنوك'), ('education', 'التعليم'), ('twafah', 'الطوافة'), ('safety', 'الأمن والسلامة'), ('farming', 'الزراعة'), ('nonprofit', 'القطاع الثالث'), ('consulting', 'الاستشارات'), ('private', 'القطاع الخاص')], default='none', max_length=50),
        ),
    ]