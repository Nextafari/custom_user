from cloudinary.models import CloudinaryField
from django.db import models
from numpy import random


def account_number_generator():
    account = random.randint(10000000)
    return account


class Traders(models.Model):
    class Meta:
        verbose_name = "Traders"
        verbose_name_plural = "Traders"

    account_number = models.IntegerField(
        max_length=10, default=account_number_generator,
    )
    name = models.CharField(max_length=200, unique=True)
    commission_type = models.CharField(max_length=200, default="revshare")
    commission_fixed_per_lot = models.IntegerField(max_length=10)
    commission_revshare = models.IntegerField(max_length=3)
    is_trial_period_enabled = models.BooleanField(default=False)
    avatar = CloudinaryField()
    experience = models.IntegerField(max_length=2)
    account_created = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=30)
    country_code = models.CharField(max_length=5)
    gain = models.DecimalField(max_digits=19, decimal_places=2)
    profit = models.DecimalField(max_digits=19, decimal_places=2)
    loss = models.DecimalField(max_digits=19, decimal_places=2)
    copiers_count = models.IntegerField(max_length=10)
    copiers_delta = models.IntegerField(max_length=10)
    time_with_us_days = models.IntegerField(max_length=50)
    is_subscribed = models.BooleanField(default=False)
    equity = models.DecimalField(max_digits=19, decimal_places=2)
    strategy_description = models.TextField()
