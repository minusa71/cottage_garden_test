# Generated by Django 4.0.3 on 2022-04-09 21:07

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_garden_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]
