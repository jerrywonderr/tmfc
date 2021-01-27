from django.db import models

# Create your models here.

class Blog_Post(models.Model):
    title = models.CharField(max_length=40, null=True, unique=True)
    sub_title = models.CharField(max_length=300, null=True)
    content = models.TextField(max_length=5000, null=True, default="Click to start typing")
    author = models.CharField(max_length=100, default="Anonymous")
    likes = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "{} by {}".format(self.title, self.author)

class Comment(models.Model):
    blog_post = models.ForeignKey(Blog_Post, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=500, null=True)
    date = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    email = models.EmailField(max_length=50, null=True)
    content = models.TextField(max_length=1000, null=True)
    date = models.DateTimeField(auto_now_add=True)
