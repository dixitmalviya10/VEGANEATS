# Generated by Django 4.0.2 on 2022-06-25 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontapp', '0004_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='c_cart',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]
