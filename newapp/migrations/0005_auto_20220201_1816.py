# Generated by Django 3.2.9 on 2022-02-01 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_auto_20220201_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image_ad',
            field=models.ImageField(upload_to='photos/ad'),
        ),
        migrations.AlterField(
            model_name='category',
            name='logo_cat',
            field=models.ImageField(upload_to='photos/category'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo_com',
            field=models.ImageField(upload_to='photos/company'),
        ),
    ]