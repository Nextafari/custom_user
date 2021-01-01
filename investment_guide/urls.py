from django.urls import path
from . import views

urlpatterns = [
    path(
        "traders/",
        views.TraderView.as_view(),
        name="traders"
    ),
    path(
        "trade_history/",
        views.TradeHistoryView.as_view(),
        name="trade_history"
    ),
    path(
        "trader_profile/<int:pk>/",
        views.TraderProfileHistoryView.as_view(),
        name="trader_profile"
    ),
    path(
        "register/",
        views.UserRegistrationView.as_view(),
        name="user_registration"
    ),
    path(
        "traders_and_history/",
        views.TraderAndHistoryView.as_view(),
        name="traders_and_history"
    )
]
