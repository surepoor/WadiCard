# Generated by Django 3.2.9 on 2022-02-06 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0005_auto_20220201_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug_cat',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='company',
            name='slug_com',
            field=models.CharField(default='none', max_length=50),
        ),
    ]