# Generated by Django 3.1.2 on 2020-12-23 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investment_guide', '0003_auto_20201214_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradehistory',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tradehistory',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
