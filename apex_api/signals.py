# from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.template.loader import render_to_string
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.conf import settings

from .models import Profile, User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Creates user profile upon user registration"""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """Saves user profile"""
    instance.profile.save()


# @receiver(reset_password_token_created)
# def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
#     """
#     Handles password reset tokens
#     When a token is created, an e-mail needs to be sent to the user
#     :param sender: View Class that sent the signal
#     :param instance: View Instance that sent the signal
#     :param reset_password_token: Token Model Object
#     :param args:
#     :param kwargs:
#     :return:
#     """
#     # send an e-mail to the user
#     context = {
#         'current_user': reset_password_token.user,
#         'email': reset_password_token.user.email,
#         'reset_password_url': "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
#     }

#     # render email text
#     email_html_message = render_to_string('email/user_reset_password.html', context)
#     email_plaintext_message = render_to_string('email/user_reset_password.txt', context)

#     msg = EmailMultiAlternatives(
#         # title:
#         "Password Reset for {title}".format(title="Some website title"),
#         # message:
#         email_plaintext_message,
#         # from:
#         "noreply@somehost.local",
#         # to:
#         [reset_password_token.user.email]
#     )
#     msg.attach_alternative(email_html_message, "text/html")
#     msg.send()

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
