from django.urls import path, include
from knox import views as knox_views
from . import views

urlpatterns = [
    path(
        'register/', views.CreateUserView.as_view(), name="user_registration"
    ),
    path(
        'login', views.UserLogin.as_view(), name="user_login"
    ),
    path(
        'transactions/', views.RecentTransactions.as_view(),
        name="recent_transactions"
    ),
    path(
        'logout/', knox_views.LogoutView.as_view(), name="knox_logout"
    ),
    # path(
    #     'logout/', views.LogoutView.as_view(), name="Logout_view"
    # ),
    # path(
    #     'user/<int:id>', views.UserDetail.as_view(), name="get_user"
    # ),
    path(
        'user_transaction', views.UserTransactionView.as_view(),
        name="user_transaction"
    ),
    path(
        'logout_all/', knox_views.LogoutAllView.as_view(), name="logout_all"
    ),
    path(
        'profile', views.UserProfile.as_view(), name="user_profile"
    ),
    path(
        'api/password_reset/',
        include('django_rest_passwordreset.urls', namespace='password_reset')
    ),
    path(
        'edit_profile/<int:id>',
        views.EditUserProfile.as_view(),
        name="edit_user"
    ),
    path('user_id', views.UserId.as_view(), name="user_id"),
    path(
        "account_linkage/",
        views.UserAccountLinkage.as_view(),
        name="user_account_linkage"
    ),
]
