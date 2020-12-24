from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from numpy import random

from .time_func import added_time, time_difference


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, name, password=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            password=password
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "User"
    username = None
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True
    )
    last_login = models.DateTimeField(
        verbose_name='last login', auto_now=True
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    # This overwrites django's default user model's username to a
    # username of choice
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.name

    def has_perm(self, perm, obj=None):
        """ Does the user have specific perimission?"""
        return self.is_admin

    def has_module_perms(self, app_label):
        """
        Does the user have specific permission to view the app'app_label'?
        """
        return True


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
    avatar = CloudinaryField("trader")
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

    def __str__(self):
        return f"{self.name}"



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
    text = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
    open_time = models.TimeField(auto_now_add=True, null=True, blank=True)
    close_time = models.TimeField(
        default=added_time(20),
        null=True,
        blank=True
    )
    duration = models.CharField(
        max_length=100,
        # default=time_difference(f"{open_time}", f"{close_time}"),
        blank=True,
        null=True
    )
    volume = models.DecimalField(max_digits=19, decimal_places=2)
    symbol = models.CharField(max_length=8)
    profit = models.DecimalField(max_digits=19, decimal_places=2)
    is_trade = models.BooleanField(default=True)
    currency = models.CharField(max_length=10, default="BTC")

    def __str__(self):
        return f"{self.trader.name}"
