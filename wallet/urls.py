from django.urls import path
from . import views


urlpatterns = [
    path('deposit/', views.Deposit.as_view(), name="deposit"),
    path('withdraw/', views.Withdraw.as_view(), name="withdraw"),
]