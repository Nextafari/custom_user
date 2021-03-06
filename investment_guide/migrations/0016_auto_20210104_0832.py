# Generated by Django 3.1.2 on 2021-01-04 08:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment_guide', '0015_auto_20210101_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='trader',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, default=3500.0, max_digits=19),
        ),
        migrations.AddField(
            model_name='trader',
            name='floating_profit',
            field=models.DecimalField(blank=True, decimal_places=2, default=1200.78, max_digits=19),
        ),
        migrations.AddField(
            model_name='trader',
            name='leverage',
            field=models.CharField(blank=True, default='1:500', max_length=250),
        ),
        migrations.AddField(
            model_name='trader',
            name='master_traders_bonus',
            field=models.DecimalField(blank=True, decimal_places=2, default=3500.0, max_digits=19),
        ),
        migrations.AlterField(
            model_name='tradehistory',
            name='close_time',
            field=models.TimeField(blank=True, default=datetime.datetime(2021, 1, 4, 8, 52, 31, 352655), null=True),
        ),
    ]
