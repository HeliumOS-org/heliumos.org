from django.contrib import admin

from .models import BlogPost, Release

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Release)
