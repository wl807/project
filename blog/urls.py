from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Item Zone
    # http://127.0.0.1:8000/blog/
    path('', views.index, name="index" ),
    # http://127.0.0.1:8000/blog/item/1
    path('item/<int:id>', views.item_detail, name="item_detail" ),
    # http://127.0.0.1:8000/blog/register/
    path('register/', views.item_register, name="item_register" ),
    # http://127.0.0.1:8000/blog/item/modify/1/
    path("item/modify/<int:pk>/", views.item_modify, name = "item_modify"),
    # http://127.0.0.1:8000/blog/item/delete/1/
    path("item/delete/<int:pk>/", views.item_delete, name = "item_delete"),











    # Question Zone
    path('qna/', views.qna, name="qna" ),
    # http://127.0.0.1:8000/blog/qna/detail/1
    path('qna/detail/<int:qid>', views.question_detail, name="question_detail" ),
    # http://127.0.0.1:8000/blog/qna/register
    path('qna/register/', views.question_register, name="question_register" ),


    # Answer Zone
    # http://127.0.0.1:8000/blog/answer/create/1/
    path("answer/create/<int:qid>/", views.answer_create, name="answer_create"),



    # Comment Zone
    # http://127.0.0.1:8000/blog/comment/create/answer/aid/
    path("comment/create/answer/<int:aid>/", views.comment_create_answer, name="comment_create_answer"),


]
