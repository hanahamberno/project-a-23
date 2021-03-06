# Generated by Django 3.1.7 on 2021-04-03 14:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('amenities', models.TextField(blank=True, default='')),
                ('address', models.CharField(blank=True, max_length=200)),
                ('furnished', models.CharField(blank=True, choices=[('furnished', 'Furnished'), ('unfurnished', 'Unfurnished')], max_length=50)),
                ('current_number_of_roommates', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('number_of_roommates_seeking', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('room_type', models.CharField(blank=True, choices=[('single', 'Single Room'), ('double', 'Double Room'), ('either', 'Either Single or Double')], max_length=50)),
                ('number_of_bedrooms', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('number_of_bathrooms', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('building_policies', models.TextField(blank=True, default='')),
                ('lease_duration', models.IntegerField(blank=True, default=12, null=True, validators=[django.core.validators.MinValueValidator(1)])),
                ('building_type', models.CharField(blank=True, choices=[('apartment', 'Apartment'), ('house', 'House'), ('townhouse', 'Townhouse'), ('other', 'Other')], max_length=50)),
                ('other_details', models.TextField(blank=True, default='')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
