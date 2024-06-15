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


class Release(models.Model):
    version = models.CharField(max_length=200, help_text="e.g. 0.0.0")
    changelog = models.TextField(help_text="Markdown")
    download_url = models.URLField(max_length=200)
    sha256 = models.CharField(max_length=200)
    torrent_url = models.CharField(max_length=200, help_text="Magnet URL")
    is_alpha = models.BooleanField(help_text="Exclusive with is_beta")
    is_beta = models.BooleanField(help_text="Exclusive with is_alpha")
    is_featured = models.BooleanField()
    image_path = models.CharField(max_length=200, help_text="e.g. /www/images/image.png")
    file_size = models.FloatField(help_text="File size in GB")
    release_date = models.DateField(help_text="Date of release")

    def __str__(self):
        return f"{self.__class__.__name__}: v{self.version}"

    class Meta:
        ordering = ["-release_date"]

