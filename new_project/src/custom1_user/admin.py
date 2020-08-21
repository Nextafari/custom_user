from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserSignUp


class UserReg(UserAdmin):
    list_display = [
       "email", "referral_code", "full_name", "date_joined", "last_login",
       "is_active", "is_admin", "is_staff", "is_superuser"
    ]

    ordering = ['email',]

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(UserSignUp, UserReg)
