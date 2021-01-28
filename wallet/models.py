from django.db import models
from apex_api.models import User


class UserAmount(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=19, default="0", decimal_places=2)

    def __str__(self):
        return f"Hello {self.user} this is your balance {self.balance}"


class Profit(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    percentage_profit_rate = models.CharField(max_length=12)
    profit = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user} your profit is {self.profit} at the \
            rate of {self.percentage_profit_rate}"
