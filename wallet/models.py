from django.db import models
from apex_api.models import User


class UserAmount(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    user_amount = models.DecimalField(max_digits=19, decimal_places=2)
