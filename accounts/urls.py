from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
# from .views import register

app_name = "accounts"

urlpatterns = [
    path(
        # http://127.0.0.1:8000/accounts/login/
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),
    path(
        # http://127.0.0.1:8000/accounts/login/
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
        #   path("logout/", views.custom_logout, name="logout"),
    # path("join/", register, name="join"),
]