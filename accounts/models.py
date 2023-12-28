from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    name = models.CharField(verbose_name="이름", max_length=64) # user의 실명 필드 추가
    nickname = models.CharField(verbose_name="닉네임", max_length=64,unique=True) # profile에 onetoone으로 연결될 unique 필드 생성
    address = models.CharField(max_length=255) # 회원가입 시 요청 필요
    phone_number = models.CharField(   # 회원가입 시 요청 필요
        max_length=13,
        verbose_name="전화번호",
        blank=True,
        validators=[RegexValidator(r"^010-[1-9]\d{3}-\d{4}$")],
        help_text="전화번호를 확인해 주세요",
    )

    is_staff = models.BooleanField(verbose_name="스태프", default=False)
    is_active = models.BooleanField(default=True) 
    objects = UserManager()
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["name"]

    def __str__(self) -> str:
        return self.email





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="프로필")

    GENDER_CHOICES = [("M", "남성"), ("F", "여성"),("N","밝히지 않음")] # gender field 선택지 설정
    gender = models.CharField(max_length=1, default="N", choices=GENDER_CHOICES)
    
    intro = models.TextField(verbose_name="자기소개", blank=True) # 자기소개 테이블
    avatar = models.ImageField(
        blank=True, default="users/default.jpeg", upload_to="users/avatar/%Y/%m/%d"
    )


# 회원가입을 하면 무조건 profile 은 생성되어야 함
# post_save,sender=User : User 가 새로 생성된 후 신호를 보내겠다
# 신호를 받는 함수 정의 : @receiver
# instance : 새롭게 생성된 User 객체 정보가 들어옴
# created : True(생성이 되었다면)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    