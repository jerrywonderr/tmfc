from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
urlpatterns = [
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("author/", views.author, name="author"),
    path("contact-us/", views.contact, name="contact"),
    path("article/<str:title>/", views.article, name="article"),
    path("page2/", views.page_two, name="page_two"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/post/delete/", views.delete_post, name="delete-post"),
    path("dashboard/post/<str:action>/", views.modify_post, name="modify-post"),

    path("login/", LoginView.as_view(
        template_name="login.html",
        redirect_authenticated_user=True
    ), name="login"),
    path("logout/", LogoutView.as_view(next_page="/home/"), name="logout"),
]