# Generated by Django 3.1.1 on 2020-11-24 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0014_product_network_connectivity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='release_date',
            field=models.CharField(default='21-10-1999', max_length=200),
        ),
    ]