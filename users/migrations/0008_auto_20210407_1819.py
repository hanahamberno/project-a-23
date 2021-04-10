# Generated by Django 3.1.7 on 2021-04-07 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_property_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='amenities',
        ),
        migrations.AddField(
            model_name='property',
            name='amenities',
            field=models.TextField(blank=True, default=''),
        ),
    ]