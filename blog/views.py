from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Blog_Post
from .forms import MessageForm, BlogPostForm
from html import unescape, escape
from django.utils.html import format_html
import re, requests

#Helper functions
def clean_html(text):
    '''Helps to strip all html tags from blog post'''
    text = text.strip()
    while True:
        md = re.compile(r".*(<.+?>).*")    #This searches a text for html tags, and groups it
        f_match = md.match(text)
        if (f_match):
            text = text.replace(f_match.groups()[0], "")    #Removes the matched html tag from text
        else:
            #If no html tags found, break loop
            break
    return text

# Create your views here.
def home(request):
    context = {}
    return render(request, "index.html", context)

def collection(request):
    context = {}
    blogs = Blog_Post.objects.all().order_by("-date")
    for field in blogs:
        field.content = format_html(clean_html(unescape(field.content[:500])))
    blog_paginator = Paginator(blogs, 6)
    page_num = request.GET.get("page")
    page_obj = blog_paginator.get_page(page_num)
    context["page_obj"] = page_obj
    context["current"] = "collections"      #This is simply for the functionality of the navigation bar
    return render(request, "collections.html", context)

def about(request):
    context = {}
    context["current"] = "about"      #This is simply for the functionality of the navigation bar
    return render(request, "about.html", context)

def contact(request):
    context = {}
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request, "Message sent successfully!")
            form = MessageForm()    #To clear previous data away from field

    context["form"] = form
    context["current"] = "contact"      #This is simply for the functionality of the navigation bar
    return render(request, "contact.html", context)
    
def article(request, title):
    context = {}
    req = "https://disqus.com/api/3.0/threads/details.json"
    blog = Blog_Post.objects.get(title=title)
    top_two = Blog_Post.objects.exclude(title=title).order_by("-date", "likes")[:4]
    for post in top_two:
        post.content = format_html(clean_html(unescape(post.content[:350])))
    blog.content = format_html(unescape(blog.content))
    context["blog"] = blog
    context["top_two"] = top_two
    context["current"] = "collections"      #This is simply for the functionality of the navigation bar
    return render(request, "article.html", context)

def author(request):
    context = {}
    return render(request, "author.html", context)

@login_required(redirect_field_name="next", login_url="/login/")
def dashboard(request):
    context = {}
    blogs = Blog_Post.objects.all().order_by("-date")
    for field in blogs:
        field.content = format_html(clean_html(unescape(field.content[:500])))
    blog_paginator = Paginator(blogs, 6)
    page_num = request.GET.get("page")
    blog_obj = blog_paginator.get_page(page_num)
    context["page_obj"] = blog_obj
    context["current"] = "dashboard"      #This is simply for the functionality of the navigation bar
    return render(request, "dashboard.html", context)

@login_required(redirect_field_name="next", login_url="/login/")
def delete_post(request):
    title = request.GET.get("title")
    if(title):
        blog = Blog_Post.objects.get(title=title)
        blog.delete()
    else:
        messages.success(request, "Error! Please refresh and try again")
    return redirect("dashboard")

@login_required(redirect_field_name="next", login_url="/login/")
def modify_post(request, action):
    context = {}
    blog_post = BlogPostForm()
    blog = {}
    if(action == "modify"):
        title = request.GET.get("title")
        blog = Blog_Post.objects.get(title=title)
        blog.content = format_html(blog.content)
        blog_post = BlogPostForm(instance=blog)
    
    if(request.method == "POST"):
        post_data = request.POST.copy()
        #post_data['content'] = unescape(request.POST.get("content"))
        if not (blog):
            blog_post = BlogPostForm(post_data)
        else:
            blog_post = BlogPostForm(post_data, instance=blog)
        if(blog_post.is_valid()):
            blog_post.save()
            return redirect("dashboard")
        else:
            print("error")
            print(blog_post.errors)
    
    context["post_form"] = blog_post
    context["current"] = "dashboard"      #This is simply for the functionality of the navigation bar
    return render(request, "modify-post.html", context)
        

