from django.contrib import admin
from .models import UserSignUp, RecentTransactions


class UserReg(admin.ModelAdmin):
    list_display = [
       "email", "referral_code", "full_name", "date_joined", "last_login",
       "is_active", "is_admin", "is_staff", "is_superuser"
    ]

admin.site.register(UserSignUp, UserReg)


class RecentTrans(admin.ModelAdmin):
    list_display = [
        "status", "date", "merchant", "transaction_type", "amount", "currency", 
        "tokens", "details"
    ]

admin.site.register(RecentTransactions, RecentTrans)
