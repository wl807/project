from django import forms
from .models import Item, Question, Answer, Comment


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["title", "content", "image", "price"]

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["subject", "content", "image"]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["content"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]

