from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from .forms import RegisterForm

# Create your views here.
def custom_logout(request):
    logout(request)
    return redirect("blog:index")



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # form.save() : form에 save() 일어난 후 model.save()
            # form.save(commit=False) : form에 save() 일어남
            user = form.save(commit=False)
            user.save()  # 모델에 추가

            # 회원가입 완료 후
            # 1) 로그인 페이지로 이동 => 사용자가 직접 로그인하기
            # return redirect("users:login")
            # 2) 로그인 처리 해주고 이동
            #    cleaned_data : is_valid() 통과한 데이터
            user = authenticate(
                request,
                username=form.cleaned_data["email"],
                password=form.cleaned_data["password1"],
            )
            if user is not None:
                login(request, user)
                return redirect("blog:index")

    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {"form": form})
