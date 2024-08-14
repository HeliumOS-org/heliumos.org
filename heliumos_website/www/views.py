from datetime import datetime

from django.core.paginator import Paginator
from django.contrib.syndication.views import Feed
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from markdown import markdown

from .models import BlogPost, Release


# Create your views here.

def index(request):
    return render(request, 'www/index.html')


def download(request):
    stable_releases = Release.objects.filter(is_alpha=False, is_beta=False, is_featured=True)
    context = {
        "releases": stable_releases,
    }
    return render(request, 'www/download.html', context)


def blog(request, page_number=1):
    all_posts = BlogPost.objects.order_by("create_date")
    paginator = Paginator(all_posts, 10)
    posts = paginator.get_page(page_number)
    context = {
        "posts": posts
    }
    return render(request, 'www/blog.html', context)


def blog_post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    rendered_content = markdown(post.content)
    create_data_iso8601 = datetime(post.create_date.year, post.create_date.month, post.create_date.day).isoformat()
    context = {
        "post": post,
        "rendered_content": rendered_content,
        "create_data_iso8601": create_data_iso8601
    }
    return render(request, 'www/blog_post.html', context)


class BlogFeed(Feed):
    title = "HeliumOS"
    link = "/blog/"
    description = "News from HeliumOS"

    def items(self):
        return BlogPost.objects.order_by("create_date")[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.summary

    def item_link(self, item):
        return reverse('blog_post', args=[item.slug])

def release_list(request, type_):
    alpha_releases = Release.objects.filter(is_alpha=True, is_featured=True)
    beta_releases = Release.objects.filter(is_beta=True, is_featured=True)
    title: str
    if type_ == "pre-release":
        title = "Download Pre-Release"
    no_releases = len(alpha_releases) + len(beta_releases) == 0
    context = {
        "title": title,
        "pre_releases": [beta_releases, alpha_releases],
        "no_releases": no_releases,
    }
    return render(request, "www/release_list.html", context)

def docs(request):
    return render(request, 'www/docs.html')

def roadmap(request):
    return render(request, "www/roadmap.html")
