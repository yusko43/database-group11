# Generated by Django 2.0.5 on 2018-05-12 08:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20180512_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 5, 12, 11, 56, 41, 285202)),
        ),
    ]
