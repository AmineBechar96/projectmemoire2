from django.shortcuts import render
from .models import *
blogs = Blog.objects
# Create your views here.
def home(request):
    return render(request,'home.html',dict(blogs=blogs))