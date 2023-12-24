
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

# 회원 가입 시 폼
# 1) ModelForm 상속 받으면서 직접 작성
# 2) UserCreationForm 상속 받기


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "name"]


