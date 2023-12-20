from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # http://127.0.0.1:8000/blog/
    path('', views.index, name="index" ),

]
