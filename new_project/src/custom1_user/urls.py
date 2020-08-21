from django.urls import path
from . import views

urlpatterns = [
    path(
        'register/', views.UserRegistration.as_view(), name="User Registration"
    ),
]