# Generated by Django 3.1.7 on 2021-04-09 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20210407_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(default='default_property.jpg', upload_to='property_pics'),
        ),
    ]
