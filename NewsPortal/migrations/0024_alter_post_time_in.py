# Generated by Django 4.0.3 on 2022-12-29 07:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPortal', '0023_post_text_en_us_post_text_ru_alter_post_time_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 29, 7, 27, 35, 111791)),
        ),
    ]
