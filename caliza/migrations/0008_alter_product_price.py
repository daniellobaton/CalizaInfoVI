# Generated by Django 4.0.4 on 2022-05-29 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caliza', '0007_product_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
