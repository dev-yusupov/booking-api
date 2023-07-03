from django.urls import path

from rest_framework.routers import DefaultRouter

from accounts.views.user_auth_view import (
    CreateUserView,
    CreateTokenView,
    ManageUserView,
    )

app_name = "accounts"

urlpatterns = [
    path("create/", CreateUserView.as_view(), name="create"),
    path("token/", CreateTokenView.as_view(), name="token"),
    path("profile/", ManageUserView.as_view(), name="authenticated-user-profile")
]
