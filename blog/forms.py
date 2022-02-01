from .models import Message, BlogPost, Comment
from django.forms import ModelForm


class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ['date']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['blocked', 'date'] 


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        exclude = ["likes", "date"]
