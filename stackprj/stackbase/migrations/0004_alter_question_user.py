# Generated by Django 4.0.3 on 2022-03-28 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stackbase', '0003_alter_question_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
