# Generated by Django 3.2.5 on 2022-05-02 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashapp', '0006_alter_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashapp.category'),
        ),
    ]