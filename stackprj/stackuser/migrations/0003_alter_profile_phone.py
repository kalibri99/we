# Generated by Django 4.0.3 on 2022-03-26 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackuser', '0002_profile_bio_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
