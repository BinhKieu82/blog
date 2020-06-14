from .models import Post, Comment
from django import forms #modelform help to save input form to database


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'author')

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content')
        # widgets = {
        #     'title': forms.TextInput(attrs={'class'}) 
        #     'slug', 
        #     'content'
        # }