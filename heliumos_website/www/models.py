from django.db import models
from django_extensions.db.fields import AutoSlugField


# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    content = models.TextField()
    slug = AutoSlugField(populate_from=["title"])
    create_date = models.DateField()

    def __str__(self):
        return f"{self.__class__.__name__}: {self.slug}"
