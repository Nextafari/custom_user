# Generated by Django 3.1.2 on 2020-12-10 14:32

from django.db import migrations, models
import investment_guide.models


class Migration(migrations.Migration):

    dependencies = [
        ('investment_guide', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trader',
            name='account_number',
            field=models.IntegerField(default=investment_guide.models.account_number_generator),
        ),
    ]
