# Generated by Django 3.2.9 on 2022-02-01 15:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_alter_category_logo_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image_ad',
            field=models.FileField(upload_to='photos/ad', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'svg'])]),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo_com',
            field=models.FileField(upload_to='photos/company', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'svg'])]),
        ),
    ]