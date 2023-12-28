from django.contrib import admin
from .models import Item, Question, Answer, Comment, Cart
from accounts.models import Profile


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "image"]
    list_display_links = ["title"]
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "item", "added_at"]
    list_display_links = ["item"]
    
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

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "gender", "intro", "avatar"]
    list_display_links = ["user"]
    pass