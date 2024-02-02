from django.core.paginator import Paginator
from django.contrib.syndication.views import Feed
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import BlogPost


# Create your views here.

def index(request):
    return render(request, 'www/index.html')


def download(request):
    return render(request, 'www/download.html')


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
    context = {
        "post": post
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
