from .models import Message, Blog_Post
from django.forms import ModelForm

class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ['date']

class BlogPostForm(ModelForm):
    class Meta:
        model = Blog_Post
        exclude = ["likes", "date"]