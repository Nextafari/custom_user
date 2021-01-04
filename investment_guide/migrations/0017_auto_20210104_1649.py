# Generated by Django 3.1.2 on 2021-01-04 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment_guide', '0016_auto_20210104_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='trader',
            name='about',
            field=models.TextField(default='Hello, I am a trader'),
        ),
        migrations.AlterField(
            model_name='tradehistory',
            name='close_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 1, 4, 17, 9, 13, 96090), null=True),
        ),
    ]
