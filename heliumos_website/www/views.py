from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'www/index.html')

def download(request):
    return render(request, 'www/download.html')
