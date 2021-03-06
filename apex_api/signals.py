# from django.core.mail import EmailMultiAlternatives
import decimal

from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.template.loader import render_to_string
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile, User, UserTransaction
from wallet.models import UserAmount


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Creates user profile upon user registration"""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """Saves user profile"""
    instance.profile.save()


"""
Signals were used to handle the calculation of the user
balance using pre save and post save.
Pre save is used to create an initial balance when the user transaction
instance is called and the post save goes on to increment the user balance
and deduct the user debit according to the transaction type while
creating the object and storing the instance in the database.
"""


@receiver(post_save, sender=User)
def create_initial_balance(sender, instance, created, **kwargs):
    if created:
        UserAmount.objects.create(
            user=instance,
            balance=0.00
        )


@receiver(post_save, sender=UserTransaction)
def save_transaction(sender, instance, created, **kwargs):
    if created:
        if instance.transaction_type == "Deposit":
            # Fetches the users latest transaction balance from the db for update
            bal_ = UserAmount.objects.filter(user=instance.user).values_list("balance").last()
            # converting a tuple from the db to a decimal
            balance = decimal.Decimal(''.join(map(str, bal_)))
            current_bal = instance.amount + balance
            UserAmount.objects.create(
                user=instance.user,
                balance=current_bal
            )

        # Fetches the users latest transaction balance from the db for update
        bal_ = UserAmount.objects.filter(user=instance.user).values_list("balance").last()
        # converting a tuple from the db to a decimal
        balance = decimal.Decimal(''.join(map(str, bal_)))
        if instance.transaction_type == "Withdrawal" and (balance) >= instance.amount:
            print("Yes This is a withdrawal and i will run the code below")
            balance -= instance.amount
            UserAmount.objects.create(
                user=instance.user,
                balance=balance
            )
        else:
            return "Not valid"


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # subject:
        "Password Reset for {title}".format(title="User Account"),
        # message:
        email_plaintext_message,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [reset_password_token.user.email]
    )
