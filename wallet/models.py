from django.db import models
from apex_api.models import User, UserTransaction


class UserAmount(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    user_amount = models.DecimalField(
        max_digits=19,
        default=UserTransaction().user_balance(),
        decimal_places=2
    )

    def __str__(self):
        return f"This is {self.user}'s balance ${self.user_amount}"
