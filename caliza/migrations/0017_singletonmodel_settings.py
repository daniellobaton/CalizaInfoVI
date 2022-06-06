# Generated by Django 4.0.4 on 2022-06-06 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caliza', '0016_oferta'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingletonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('singletonmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='caliza.singletonmodel')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='caliza.customer')),
            ],
            bases=('caliza.singletonmodel',),
        ),
    ]