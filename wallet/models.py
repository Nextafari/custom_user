from django.db import models
from apex_api.models import User, UserTransaction
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserAmount(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=19, default="0", decimal_places=2)

    def __str__(self):
        return f"Hello {self.user} this is your balance {self.balance}"
