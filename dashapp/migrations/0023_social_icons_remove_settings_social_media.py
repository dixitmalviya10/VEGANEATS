# Generated by Django 4.0.2 on 2022-06-17 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashapp', '0022_remove_settings_social_media2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='social_icons',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('social_media', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='settings',
            name='social_media',
        ),
    ]
