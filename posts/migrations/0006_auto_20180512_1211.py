# Generated by Django 2.0.5 on 2018-05-12 09:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20180512_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 12, 12, 11, 13, 113226)),
        ),
    ]
