# Generated by Django 3.1.12 on 2023-10-14 03:34

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_sliders_colorbackground'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sliders',
            name='colorBackground',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None, verbose_name='color'),
        ),
    ]
