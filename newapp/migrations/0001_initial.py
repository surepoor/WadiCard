# Generated by Django 3.2.9 on 2022-01-30 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_hero', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('logo_header', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('join_us', models.URLField(max_length=150)),
            ],
        ),
    ]