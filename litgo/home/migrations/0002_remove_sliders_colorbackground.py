# Generated by Django 3.1.12 on 2023-10-14 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sliders',
            name='colorBackground',
        ),
    ]
