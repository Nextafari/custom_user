# Generated by Django 3.1.2 on 2020-12-23 23:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment_guide', '0008_auto_20201223_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradehistory',
            name='close_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 12, 24, 0, 14, 12, 895743), null=True),
        ),
    ]
