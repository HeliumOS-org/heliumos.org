from django.contrib import admin

from .models import BlogPost, QuestionAnswer, Release

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(QuestionAnswer)
admin.site.register(Release)
