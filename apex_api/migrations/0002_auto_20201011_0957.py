# Generated by Django 3.1.2 on 2020-10-11 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apex_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertransaction',
            name='amount',
            field=models.DecimalField(decimal_places=8, max_digits=10),
        ),
    ]
