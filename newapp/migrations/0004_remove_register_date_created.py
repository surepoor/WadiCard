# Generated by Django 3.2.9 on 2022-02-24 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_register'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='date_created',
        ),
    ]
