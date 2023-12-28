from django.urls import path, re_path
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
        # http://127.0.0.1:8000/accounts/logout/
    # custom logout : post 형식만 가능..
    path("logout/", views.custom_logout, name="logout"),
        # http://127.0.0.1:8000/accounts/join/
    path("join/", views.register, name="join"),


     # My Page
    # http://127.0.0.1:8000/accounts/유저이름/mypage/
    # path("mypage/", views.mypage, name="mypage"),

    re_path(r"^(?P<nickname>[\w.@+-]+)/mypage/", views.mypage, name="mypage"), # re_path 하기
]