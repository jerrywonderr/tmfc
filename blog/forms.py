from .models import Message, BlogPost
from django.forms import ModelForm


class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ['date']


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        exclude = ["likes", "date"]
