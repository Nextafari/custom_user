from django.urls import path
from . import views

urlpatterns = [
    path(
        'register/', views.CreateUserView.as_view(), name="User Registration"
    ),
    path(
        'login/', views.UserLogin.as_view(), name="User login"
    ),
    path(
        'transactions/', views.RecentTransactions.as_view(), 
        name="Recent Transactions"
    )
]
