# Generated by Django 3.1.7 on 2021-04-15 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20210415_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='match_list',
            field=models.CharField(blank=True, choices=[('Property', 'Have a property'), ('Profile', "Don't have a property"), ('Both', 'No preference')], max_length=100, verbose_name='Match with people who'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pref_gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('no preference', 'No preference')], max_length=30, verbose_name='Preferred Gender'),
        ),
    ]