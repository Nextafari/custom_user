from django.contrib import admin
from .models import User, RecentTransaction, UserReferralLink


class UserReg(admin.ModelAdmin):
    list_display = [
       "email", "full_name", "date_joined", "last_login",
       "is_active", "is_admin", "is_staff", "is_superuser"
    ]


admin.site.register(User, UserReg)


class UserRefLink(admin.ModelAdmin):
    list_diplay = ["referral_link"]


admin.site.register(UserReferralLink, UserRefLink)


class RecentTrans(admin.ModelAdmin):
    list_display = [
        "status", "date", "merchant", "transaction_type", "amount", "currency",
        "tokens", "details"
    ]


admin.site.register(RecentTransaction, RecentTrans)
