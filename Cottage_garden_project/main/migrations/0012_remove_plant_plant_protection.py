# Generated by Django 4.0.3 on 2022-04-09 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_garden_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='plant_protection',
        ),
    ]
