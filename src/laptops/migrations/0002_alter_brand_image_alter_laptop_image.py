# Generated by Django 5.0.7 on 2024-08-09 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptops', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='staticfiles/img/brand_imgs'),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='staticfiles/img/laptop_imgs'),
        ),
    ]
