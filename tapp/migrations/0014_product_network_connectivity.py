# Generated by Django 3.1.1 on 2020-11-24 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0013_auto_20201116_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='network_connectivity',
            field=models.CharField(default='LTE', max_length=200),
        ),
    ]