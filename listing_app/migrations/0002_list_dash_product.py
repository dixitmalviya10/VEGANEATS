# Generated by Django 4.0.2 on 2022-05-30 04:49

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashapp', '0018_alter_checkout_details_states'),
        ('listing_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='list_dash_product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.ImageField(blank=True, null=True, upload_to='products')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('product_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashapp.category')),
            ],
        ),
    ]