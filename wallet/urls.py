from django.urls import path
from . import views


urlpatterns = [
    path('deposit/', views.Deposit.as_view(), name="deposit"),
    path('withdraw/', views.Withdraw.as_view(), name="withdraw"),
    path('user_amount', views.UserAmountView.as_view(), name="user_amount"),
    path('user_profit', views.UserProfitView.as_view(), name="user_profit"),
    path(
        "processing_fee",
        views.WithdrawalFee.as_view(),
        name="withdrawal_fee"
    ),
    path(
        "compound_profit/",
        views.CompoundedProfit.as_view(),
        name="compound_profit"
    ),
]
