# Generated by Django 3.1.12 on 2023-10-12 14:23

import colorfield.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aboutus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='footers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor_hp', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Nomor telepon harus dimulai dengan '08' dan memiliki panjang minimal 10 karakter (termasuk '08').", regex='^08\\d{8,}$')])),
                ('link_instagram', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message="URL tidak valid. Pastikan formatnya benar, seperti 'http://www.example.com'.", regex='^(http|https)://[a-zA-Z0-9.-]+(\\.[a-zA-Z]{2,4})(:[0-9]+)?(/.*)?$')])),
                ('link_tokopedia', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message="URL tidak valid. Pastikan formatnya benar, seperti 'http://www.example.com'.", regex='^(http|https)://[a-zA-Z0-9.-]+(\\.[a-zA-Z]{2,4})(:[0-9]+)?(/.*)?$')])),
                ('link_blibli', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message="URL tidak valid. Pastikan formatnya benar, seperti 'http://www.example.com'.", regex='^(http|https)://[a-zA-Z0-9.-]+(\\.[a-zA-Z]{2,4})(:[0-9]+)?(/.*)?$')])),
                ('link_shopee', models.CharField(max_length=200, validators=[django.core.validators.RegexValidator(message="URL tidak valid. Pastikan formatnya benar, seperti 'http://www.example.com'.", regex='^(http|https)://[a-zA-Z0-9.-]+(\\.[a-zA-Z]{2,4})(:[0-9]+)?(/.*)?$')])),
            ],
        ),
        migrations.CreateModel(
            name='sliders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleImage', models.CharField(max_length=256)),
                ('image', models.ImageField(upload_to='static/img')),
                ('descImage', models.TextField()),
                ('colorBackground', colorfield.fields.ColorField(blank=True, default='', image_field='image', max_length=25, samples=None)),
            ],
        ),
    ]
