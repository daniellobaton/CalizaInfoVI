# Generated by Django 4.0.4 on 2022-06-03 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caliza', '0011_getproducts'),
    ]

    operations = [
        migrations.AddField(
            model_name='getproducts',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
