# Generated by Django 3.1.7 on 2021-04-15 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_property_on_grounds'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='pref_gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('no preference', 'No preference')], max_length=30),
        ),
    ]
