from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def custom_logout(request):
    logout(request)
    return redirect("blog:index")