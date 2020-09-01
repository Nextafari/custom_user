from django.urls import path
from knox import views as knox_views
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
    ),
    # path(
    #     'logout', knox_views.LogoutView.as_view(), name="Log out"
    # ),
    path(
        'logout', views.LogoutView.as_view(), name="Logout view"
    ),
    path(
        'dashboard/', views.template_view, name="Dash board"
    ),
    path(
        'logout_all/', knox_views.LogoutAllView.as_view(), name="Log out all"
    )
]
