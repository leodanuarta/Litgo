# Generated by Django 3.1.12 on 2023-11-13 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20231111_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sliders',
            name='colorBackground',
        ),
    ]
