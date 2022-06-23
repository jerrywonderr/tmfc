from django.shortcuts import get_object_or_404
from .models import Message, BlogPost, Comment
from django.forms import ModelForm


class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ['date']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ['blog_post', 'blocked', 'date'] 
    
    def save(self, blog, commit=True):
        if not blog:
            raise ValueError('Blog object must be specified')
        comment = super(CommentForm, self).save(commit=False)
        comment.blog_post = blog
        if commit:
            comment.save()
            
        return commit


class BlogPostForm(ModelForm):
    class Meta:
        model = BlogPost
        exclude = ["likes", "date"]
    
    # def save(self, commit=True):
    #     blog_post = super().save(commit=False)
        
