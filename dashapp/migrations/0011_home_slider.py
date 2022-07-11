# Generated by Django 3.2.5 on 2022-05-04 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashapp', '0010_alter_settings_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='home_slider',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slider_image', models.ImageField(blank=True, null=True, upload_to='slider_images')),
                ('slider_heading', models.CharField(max_length=100)),
                ('slider_subheading', models.CharField(max_length=100)),
            ],
        ),
    ]
