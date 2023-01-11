# Generated by Django 4.0.3 on 2022-12-19 11:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPortal', '0022_alter_post_time_in_alter_postcategory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text_en_us',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='text_ru',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 19, 11, 0, 32, 462928)),
        ),
    ]