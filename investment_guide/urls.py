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
]
