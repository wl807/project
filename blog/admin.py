from django.contrib import admin
from .models import Item, Question, Answer, Comment


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "image"]
    list_display_links = ["title"]
    
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "subject", "author"]
    list_display_links = ["subject"]

    
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "content", "author"]
    list_display_links = ["content"]
    pass