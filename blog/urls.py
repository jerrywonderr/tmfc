from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("collections/", views.collection, name="collection"),
    path("about/", views.about, name="about"),
    path("author/", views.Author.as_view(), name="author"),
    path("contact-us/", views.contact, name="contact"),
    path("article/", views.AdminArticle.as_view(), name="admin-article"),
    path("article/<str:title>/", views.Article.as_view(), name="article"),
    path("comment/<str:title>/", views.Comment.as_view(), name="comment"),
    # path("article/comments/<str:title>", views.add_comment, name="comment"),
    path("dashboard/", views.dashboard, name="dashboard"),

    path("login/", LoginView.as_view(
        template_name="login.html",
        redirect_authenticated_user=True
    ), name="login"),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
]
