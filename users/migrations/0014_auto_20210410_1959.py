# Generated by Django 3.1.7 on 2021-04-10 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20210410_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.CharField(blank=True, max_length=200, verbose_name='Address/Location'),
        ),
    ]
