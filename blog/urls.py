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
    # http://127.0.0.1:8000/blog/qna/
    path('qna/', views.qna, name="qna" ),
    # http://127.0.0.1:8000/blog/faq
    path('faq/', views.faq, name="faq" ),
    # http://127.0.0.1:8000/blog/qna/detail/1
    path('qna/detail/<int:qid>', views.question_detail, name="question_detail" ),
    # http://127.0.0.1:8000/blog/qna/register
    path('qna/register/', views.question_register, name="question_register" ),
    # http://127.0.0.1:8000/blog/qna/modify
    path('qna/modify/<int:qid>', views.question_modify, name="question_modify" ),
    # http://127.0.0.1:8000/blog/qna/delete
    path('qna/delete/<int:qid>', views.question_delete, name="question_delete" ),




    # Answer Zone
    # http://127.0.0.1:8000/blog/answer/create/1/
    path("answer/create/<int:qid>/", views.answer_create, name="answer_create"),
    # http://127.0.0.1:8000/blog/answer/delete/1/
    path("answer/delete/<int:aid>/", views.answer_delete, name="answer_delete"),
    # http://127.0.0.1:8000/blog/answer/modify/1/
    path("answer/modify/<int:aid>/", views.answer_modify, name="answer_modify"),



    # Comment Zone
    # http://127.0.0.1:8000/blog/comment/create/answer/aid/
    path("comment/create/answer/<int:aid>/", views.comment_create_answer, name="comment_create_answer"),
    # http://127.0.0.1:8000/blog/comment/modify/answer/aid/
    path("comment/modify/answer/<int:cid>/", views.comment_modify_answer, name="comment_modify_answer"),
    # http://127.0.0.1:8000/blog/comment/delete/answer/aid/
    path("comment/delete/answer/<int:cid>/", views.comment_delete_answer, name="comment_delete_answer"),


]
