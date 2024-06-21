from django.contrib.sitemaps import Sitemap
from django.urls.base import reverse

from .models import BlogPost
from .views import download, docs, index


class MainSitemap(Sitemap):
    def items(self):
        return [download, docs, index]

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    def items(self):
        return BlogPost.objects.filter(is_published=True)

sitemaps = {
    "main": MainSitemap,
    "blog": BlogSitemap
}
