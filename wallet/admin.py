from django.contrib import admin
from .models import UserAmount


class UserAmountAdmin(admin.ModelAdmin):
    list_display = [
        "user", "user_amount"
    ]


admin.site.register(UserAmount, UserAmountAdmin)
