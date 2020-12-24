from django.contrib import admin
from .models import Trader, TradeHistory, User


class TraderDBView(admin.ModelAdmin):
    list_display = [
        "name", "commission_type", "commission_fixed_per_lot",
        "commission_revshare", "is_trial_period_enabled", "avatar",
        "experience", "account_created", "country", "country_code",
        "gain", "profit", "loss", "copiers_count", "copiers_delta",
        "time_with_us_days", "is_subscribed", "equity", "strategy_description"
    ]


admin.site.register(Trader, TraderDBView)


class TraderHistroyDb(admin.ModelAdmin):
    list_display = [
        "trader", "icon", "text", "date", "open_time",
        "close_time", "duration", "volume", "symbol", 
        "profit", "is_trade", "currency"
    ]


admin.site.register(TradeHistory, TraderHistroyDb)


class UsersReg(admin.ModelAdmin):
    list_display = [
       "email", "name", "date_joined", "last_login",
       "is_active", "is_admin", "is_staff", "is_superuser"
    ]


admin.site.register(User, UsersReg)
