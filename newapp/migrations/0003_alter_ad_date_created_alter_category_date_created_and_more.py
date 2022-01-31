# Generated by Django 4.0 on 2022-01-31 14:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_ad_category_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 31, 17, 40, 57, 332493)),
        ),
        migrations.AlterField(
            model_name='category',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 31, 17, 40, 57, 330494)),
        ),
        migrations.AlterField(
            model_name='company',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 31, 17, 40, 57, 331494)),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.IntegerField(max_length=15),
        ),
    ]
