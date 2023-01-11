# Generated by Django 4.0.3 on 2022-12-17 01:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPortal', '0018_alter_post_time_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='name of Category of post', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 17, 1, 54, 24, 71093)),
        ),
    ]
