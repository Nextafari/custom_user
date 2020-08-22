from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Valid email should be provided")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Valid email should be provided")
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_superuser'] = True
        extra_fields['is_staff'] = True

        if extra_fields.get('is_superuser') and extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must have is_superuser and is_staff=True.')

        return self._create_user(email, password, **extra_fields)



class User(AbstractBaseUser,PermissionsMixin):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["full_name"]

    class Meta:
        verbose_name = "User Sign Up"
        verbose_name_plural = "User Sign Up"
    email = models.EmailField(unique=True)
    referral_code = models.CharField(max_length=250, blank=True)
    full_name = models.CharField(max_length=50)
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

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        """ Does the user have specific perimission?"""
        return self.is_admin

    def has_module_perms(self, app_label):
        """ 
        Does the user have specific permission to view the app'app_label'?
        """
        return True


class RecentTransactions(models.Model):
    class Meta:
        verbose_name = "Recent Transactions"
        verbose_name_plural = "Recent Transactions"
    STATUS_CHOICES = (
        ("Paid", "Paid"),
        ("Unpaid", "Unpaid")
    )
    TRANSACTION_TYPE_CHOICES = (
        ("Deposit", "Deposit"),
        ("Withdrawal", "Withdrawal")
    )
    CURRENCY_CHOICES = (
        ("ETH", "ETH"),
        ("BTC", "BTC")
    )
    DETAIL_CHOICES = (
        ("Deposit to wallet", "Deposit to wallet"),
        ("Withdrawal from wallet", "Withdrawal from wallet")
    )
    
    status = models.CharField(max_length=60, choices=STATUS_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    merchant = models.CharField(max_length=60)
    transaction_type = models.CharField(
        max_length=60, choices=TRANSACTION_TYPE_CHOICES
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=5, choices=CURRENCY_CHOICES)
    tokens = models.DecimalField(max_digits=9, decimal_places=2)
    details = models.CharField(max_length=100, choices=DETAIL_CHOICES)

    def __str__(self):
        return self.merchant
