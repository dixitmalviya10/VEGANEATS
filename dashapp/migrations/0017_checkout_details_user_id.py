# Generated by Django 3.2.5 on 2022-05-16 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashapp', '0016_checkout_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout_details',
            name='user_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
