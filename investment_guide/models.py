from cloudinary.models import CloudinaryField
from django.db import models
from numpy import random


def account_number_generator():
    account = random.randint(10000000)
    return account


class Trader(models.Model):
    class Meta:
        verbose_name = "Traders"
        verbose_name_plural = "Traders"

    account_number = models.IntegerField(
        default=account_number_generator
    )
    name = models.CharField(max_length=200, unique=True)
    commission_type = models.CharField(max_length=200, default="revshare")
    commission_fixed_per_lot = models.IntegerField()
    commission_revshare = models.IntegerField()
    is_trial_period_enabled = models.BooleanField(default=False)
    avatar = CloudinaryField()
    experience = models.IntegerField()
    account_created = models.DateTimeField(auto_created=True)
    country = models.CharField(max_length=30)
    country_code = models.CharField(max_length=5)
    gain = models.DecimalField(max_digits=19, decimal_places=2)
    profit = models.DecimalField(max_digits=19, decimal_places=2)
    loss = models.DecimalField(max_digits=19, decimal_places=2)
    copiers_count = models.IntegerField()
    copiers_delta = models.IntegerField()
    time_with_us_days = models.IntegerField()
    is_subscribed = models.BooleanField(default=False)
    equity = models.DecimalField(max_digits=19, decimal_places=2)
    strategy_description = models.TextField()


class TradeHistory(models.Model):
    class Meta:
        verbose_name = "Trade History"
        verbose_name_plural = "Trade Histories"

    ICON_CHOICES = (
        ("sell", "sell"),
        ("buy", "buy")
    )

    trader = models.ForeignKey(
        to=Trader, null=True, on_delete=models.SET_NULL
    )
    icon = models.CharField(
        max_length=15, choices=ICON_CHOICES
    )
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    open_time = models.TimeField(auto_now_add=True)
    close_time = models.TimeField(auto_now_add=True)
    duration = models.DurationField(blank=True)
    volume = models.DecimalField(max_digits=19, decimal_places=2)
    symbol = models.CharField(max_length=8)
    profit = models.DecimalField(max_digits=19, decimal_places=2)
    is_trade = models.BooleanField(default=True)
    currency = models.CharField(max_length=10, default="BTC")
