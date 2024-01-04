from django.contrib import admin
from .models import Item, Question, Answer, Comment, Cart,CartItem
from accounts.models import Profile


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "image"]
    list_display_links = ["title"]




@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user")
    # def display_items(self, obj):
    #     return ", ".join([str(item) for item in obj.item.all()])
    # display_items.short_description = 'Items'
    
    list_display_links = ["user"]
    

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("id", "cart", "item", "added_at")
    def display_items(self, obj):
        return ", ".join([str(item) for item in obj.item.all()])
    display_items.short_description = 'Items'
    
    list_display_links = ["cart"]



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