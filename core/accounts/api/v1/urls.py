from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

# from rest_framework.authtoken.views import ObtainAuthToken

from . import views

app_name = "api-V1"

urlpatterns = [
    path(
        "registration/",
        views.RegistrationApiView.as_view(),
        name="registration",
    ),
    path("token/login/", views.CustomAuthToken.as_view(), name="token-login"),
    path(
        "token/logout/",
        views.CustomDiscardAuthToken.as_view(),
        name="token-logout",
    ),
    # send email
    # path('test-email/', views.TestEmailSend.as_view(), name='test-email'),
    # confirm email
    path(
        "activation/confirm/<str:token>/",
        views.ActivationApiView.as_view(),
        name="activation",
    ),
    # resend activation
    path(
        "activation/resend/",
        views.ActivationResendApiView.as_view(),
        name="activation-resend",
    ),
    # change password
    path(
        "change-password/",
        views.ChangePasswordApiView.as_view(),
        name="change-password",
    ),
    # jwt path
    path(
        "jwt/create/",
        views.CustomTokenObtainPairView.as_view(),
        name="jwt-create",
    ),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    # profile
    path("profile/", views.ProfileApiView.as_view(), name="profile"),
]
