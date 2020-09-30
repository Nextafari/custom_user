from django.contrib import admin
from .models import UserAmount, Profit


class UserAmountAdmin(admin.ModelAdmin):
    list_display = [
        "user", "balance"
    ]


admin.site.register(UserAmount, UserAmountAdmin)


class UserProfit(admin.ModelAdmin):
    list_display = [
        "percentage_profit_rate", "profit"
    ]


admin.site.register(Profit, UserProfit)
