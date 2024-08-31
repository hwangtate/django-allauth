from django.urls import path, include
from . import views

urlpatterns = [
    path("accounts/signup/", view=views.account_signup_view),
    path("accounts/", include("allauth.urls")),
]
