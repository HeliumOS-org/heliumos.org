from django.core.paginator import Paginator
from django.contrib.sitemaps.views import sitemap
from django.urls import path

from . import views
from .models import BlogPost
from .sitemaps import sitemaps


urlpatterns = [
    path("", views.index, name="index"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("download/", views.download, name="download"),
    path("blog/", views.blog, name="blog"),
    path("blog/page/<int:page_number>/", views.blog, name="blog"),
    path("blog/post/<str:slug>/", views.blog_post, name='blog_post'),
    path("feed.xml", views.BlogFeed(), name="feed"),
    path("releases/<str:type_>/", views.release_list, name="release_list"),
    path("docs/", views.docs, name="docs"),
    path("roadmap/", views.roadmap, name="roadmap"),
    path("hardware/", views.hardware, name="hardware"),
]
