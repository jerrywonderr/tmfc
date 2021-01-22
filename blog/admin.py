from django.contrib import admin
from .models import Comment, Blog_Post, Message

# Register your models here.
@admin.register(Blog_Post)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'likes', 'date']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['blog_post', 'text']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['email', 'content']

