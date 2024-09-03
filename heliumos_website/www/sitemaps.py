from django.contrib.sitemaps import Sitemap
from django.urls.base import reverse

from .models import BlogPost
from .views import download, docs, hardware, index, roadmap


class MainSitemap(Sitemap):
    def items(self):
        return [download, docs, index, roadmap, hardware]

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    def items(self):
        return BlogPost.objects.filter(is_published=True)

sitemaps = {
    "main": MainSitemap,
    "blog": BlogSitemap
}
