# Generated by Django 3.1.1 on 2020-09-25 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0005_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]