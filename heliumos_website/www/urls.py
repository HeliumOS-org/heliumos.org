from django.urls import path
from django_distill import distill_path

from . import views

urlpatterns = [
    distill_path("", views.index, name="index"),
    distill_path("download", views.download, name="download")
]