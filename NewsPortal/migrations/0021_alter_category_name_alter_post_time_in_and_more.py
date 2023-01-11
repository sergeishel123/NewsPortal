# Generated by Django 4.0.3 on 2022-12-17 02:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPortal', '0020_alter_post_time_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='имя Категории новости', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_in',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 17, 2, 19, 24, 753896)),
        ),
        migrations.AlterField(
            model_name='postcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPortal.category', verbose_name='This is help text'),
        ),
    ]
