from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View, TemplateView
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse
from .models import BlogPost, Comment
from .forms import CommentForm, MessageForm, BlogPostForm
from html import unescape, escape
from django.utils.html import format_html
import re


# Helper functions
def cleans_html(text):
    """Helps to strip all html tags from blog post"""
    text = text.strip()
    while True:
        md = re.compile(r".*(<.+?>).*")    # This searches a text for html tags, and groups it
        f_match = md.match(text)
        if f_match:
            text = text.replace(f_match.groups()[0], "")    # Removes the matched html tag from text
        else:
            # If no html tags found, break loop
            break
    return text


# Create your views here.
def home(request):
    context = {}
    return render(request, "index.html", context)


def collection(request):
    context = {}
    blogs = BlogPost.objects.all().filter(public=True).order_by("-date")
    blog_paginator = Paginator(blogs, 6)
    page_num = request.GET.get("page")
    page_obj = blog_paginator.get_page(page_num)
    context["page_obj"] = page_obj
    context["current"] = "collections"      # This is simply for the functionality of the navigation bar
    return render(request, "collections.html", context)


def about(request):
    context = {"current": "about"}  # This is simply for the functionality of the navigation bar
    return render(request, "about.html", context)


def contact(request):
    context = {}
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully!")
            form = MessageForm()    # To clear previous data away from field

    context["form"] = form
    context["current"] = "contact"      # This is simply for the functionality of the navigation bar
    return render(request, "contact.html", context)

class Article(View):

    def get(self, request, title):
        try:
            blog = get_object_or_404(BlogPost, title=title)
            blog.content = format_html(unescape(blog.content))
            top_three_blog = BlogPost.objects.exclude(title=title, public=False).order_by("-date", "likes")[:4]
            comment_form = CommentForm()
        except Exception as e:
            raise Http404()
        
        context = {
            'blog': blog,
            'top_two': top_three_blog,
            'comment_form': comment_form,
            'current': 'collections'
        }
        
        return render(request, "article.html", context)


class AdminArticle(View):

    @method_decorator(login_required(redirect_field_name="next", login_url="/login/"))
    def delete(self, request):
        title = request.GET.get("title")
        response = {
            'ok': False,
        }
        try:
            blog = BlogPost.objects.get(title=title)
            response['ok'] = True
            blog.delete()
            messages.success(request, f"{blog.title} successfully deleted!")

        except Exception as e:
            # response['message'] = e
            messages.error(request, "Error! Please refresh and try again")
        return JsonResponse(response)
    
    @method_decorator(login_required(redirect_field_name="next", login_url="/login/"))
    def get(self, request):
        title = request.GET.get('title')
        print('get request')
        blog_form = self.get_post_form(title)

        context = {
            "post_form": blog_form,
            "blog_title": title,
            "current": "dashboard"  # This is simply for the functionality of the navigation bar
        }

        return render(request, "modify-post.html", context)

    @method_decorator(login_required(redirect_field_name="next", login_url="/login/"))
    def post(self, request):

        title = request.GET.get('title')
        blog_exists = BlogPost.objects.filter(title=title).count()
        data = request.POST.copy()
        data['content'] = escape(data['content'])
        new_entry = False if blog_exists else True
        blog_form = self.get_post_form(title, data, new_entry)

        if blog_form.is_valid():
            blog_form.save()
        else:
            context = {
                "post_form": blog_form,
                "blog_title": title,
                "current": "dashboard" # This is simply for the functionality of the navigation bar
            }

            return render(request, "modify-post.html", context)
        
        return redirect('dashboard')
    
    def get_post_form(self, title, form_data={}, new_entry=False):
        if not new_entry:
            blog_instance = BlogPost.objects.get(title=title)
            blog_instance.content = format_html(unescape(blog_instance.content))
            # Bring up form with the right blog object as instance
            if form_data:
                blog_form = BlogPostForm(form_data, instance=blog_instance)
            else: 
                blog_form = BlogPostForm(instance=blog_instance)
        elif form_data:
            # Most likely we are trying to create a new entry with form_data
            blog_form = BlogPostForm(form_data)
        else:
            # Then we need an empty form for creating new entry
            blog_form = BlogPostForm()
                
        return blog_form


class Comment(View):

    def post(self, request, title):
        try:
            blog = get_object_or_404(BlogPost, title=title)
            top_three_blog = BlogPost.objects.exclude(title=title, public=False).order_by("-date", "likes")[:4]
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment_form.save(blog=blog)
                messages.success(request, 'Comment added')
            else:
                context = {
                    'blog': blog,
                    'top_two': top_three_blog,
                    'comment_form': comment_form,
                    'current': 'collections'
                }
                return render(request, "article.html", context)
        except Exception as e:
            raise Http404()
        
        return redirect('article', title=blog.title)
    
    @method_decorator(login_required(redirect_field_name="next", login_url="/login/"))
    def delete(request, id):
        try:
            comment = get_object_or_404(Comment, id=id)
            comment.delete()
        except Exception as e:
            messages.error(request, "Error! Please refresh and try again")
        return redirect(request.META['HTTP_REFERER'])


class Author(TemplateView):
    template_name = 'author.html'


@login_required(redirect_field_name="next", login_url="/login/")
def dashboard(request):
    context = {}
    blogs = BlogPost.objects.all().order_by("-date")
    blog_paginator = Paginator(blogs, 6)
    page_num = request.GET.get("page")
    blog_obj = blog_paginator.get_page(page_num)
    context["page_obj"] = blog_obj
    context["current"] = "dashboard"      # This is simply for the functionality of the navigation bar
    return render(request, "dashboard.html", context)
