from django.contrib import admin
from .models import (
    User, RecentTransaction, UserTransaction,
    Profile
)
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy


AdminSite.site_title = gettext_lazy('TRDDEX')

# Text to put in each page's <h1>.
AdminSite.site_header = gettext_lazy('TRDDEX ADMIN')

# Text to put at the top of the admin index page.
AdminSite.index_title = gettext_lazy('TRDDEX ADMIN')


class UserReg(admin.ModelAdmin):
    list_display = [
        "email", "full_name", "date_joined", "last_login",
        "investor", "is_active", "is_admin", "is_staff",
        "is_superuser"
    ]


admin.site.register(User, UserReg)


class RecentTrans(admin.ModelAdmin):
    list_display = [
        "status", "date", "merchant", "transaction_type", "amount", "currency",
        "tokens", "details"
    ]


admin.site.register(RecentTransaction, RecentTrans)


class UserTrans(admin.ModelAdmin):
    list_display = [
        'user', 'date', 'transaction_type', 'amount', 'payment_method',
        'amount_in_btc', 'details'
    ]


admin.site.register(UserTransaction, UserTrans)


class UserProfile(admin.ModelAdmin):
    list_display = [
        "user", "image", "trading_code"
    ]


admin.site.register(Profile, UserProfile)
