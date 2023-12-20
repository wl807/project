from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

# 회원 앱 필요하다면?
# 장고 User 사용 - django.contrib.auth.models.User
# 직접 작성 - 1. 장고 User 상속 받으면서 새로 작성
#             2. 새로 작성


class UserManager(BaseUserManager):
    def _create_user(self, email, password, name, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password, name, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_staff", False)

        return self._create_user(email, password, name, **extra_fields)

    def create_superuser(self, email, password, name, **extra_fields):
        """
        python manage.py createsuperuser 호출
        """
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        return self._create_user(email, password, name, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    email(username 개념),password,name,gender(선택사항)
    AbstractBaseUser - password, last_login,is_active = True
    is_staff (어드민 사이트 접근시 요구되는 값)
    """

    email = models.EmailField(verbose_name="이메일", max_length=150, unique=True)
    name = models.CharField(verbose_name="이름", max_length=64)
    is_staff = models.BooleanField(verbose_name="스태프", default=False)
    is_active = models.BooleanField(default=True) 


    objects = UserManager()
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["name"]

    def __str__(self) -> str:
        return self.email
