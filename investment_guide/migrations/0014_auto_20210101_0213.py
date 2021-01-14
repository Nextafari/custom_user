# Generated by Django 3.1.2 on 2021-01-01 02:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment_guide', '0013_auto_20210101_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='trader',
            name='minimum_value',
            field=models.DecimalField(decimal_places=2, default=200.0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='tradehistory',
            name='close_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 1, 1, 2, 33, 19, 253727), null=True),
        ),
    ]