from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from accounts.views.user_auth_view import (
    CreateUserView,
    CreateTokenView,
    ManageUserView,
    )

app_name = "accounts"

urlpatterns = [
    path("signup/", CreateUserView.as_view(), name="signup"),
    path("token/", CreateTokenView.as_view(), name="token"),
    path("profile/", ManageUserView.as_view(), name="profile"),
]
