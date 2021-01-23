from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import random
import string
from cloudinary.models import CloudinaryField


class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, full_name, password=None, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            full_name=full_name,
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
    full_name = models.CharField(max_length=50)
    investor = models.BooleanField(
        default=False, blank=True
    )
    account_linked = models.BooleanField(default=False)
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
    REQUIRED_FIELDS = ["full_name"]

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


class RecentTransaction(models.Model):
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
        ("Ξ ETH", "Ξ ETH"),
        ("฿ BTC", "฿ BTC")
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


class UserTransaction(models.Model):
    class Meta:
        verbose_name = "User Transactions"
        verbose_name_plural = "User Transactions"
    TRANSACTION_TYPE_CHOICES = (
        ("Deposit", "Deposit"),
        ("Withdrawal", "Withdrawal")
    )
    DETAIL_CHOICES = (
        ("Deposit to wallet", "Deposit to wallet"),
        ("Withdrawal from wallet", "Withdrawal from wallet")
    )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    transaction_type = models.CharField(
        max_length=200, choices=TRANSACTION_TYPE_CHOICES
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default="Pending")
    amount_in_btc = models.DecimalField(max_digits=10, decimal_places=4)
    details = models.CharField(max_length=200, choices=DETAIL_CHOICES)

    def __str__(self):
        return self.transaction_type


def create_trading_code():
    """Generates trading code for user"""
    letters = string.ascii_lowercase
    length = 5
    num = random.randrange(0, 10)
    code_str_int = ''.join(
        random.choice(letters+str(num)) for i in range(length)
    )
    return code_str_int


class Profile(models.Model):
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField("profile_pics", default="fdhdfs.jpg")
    trading_code = models.CharField(
        max_length=10, default=create_trading_code, blank=True
    )

    def __str__(self):
        return f"{self.user.full_name} Profile"
