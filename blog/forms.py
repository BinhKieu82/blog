from .models import Comment
from django import forms #modelform help to save input form to database


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')