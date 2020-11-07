from django.shortcuts import render,get_object_or_404
from .models import *

# Create your views here.
def home(request):
    blogs1 = Blog.objects
    return render(request, 'home.html', dict(blogs=blogs1))


def blogs(request):
    blogs2 = Blog.objects
    return render(request, 'blog.html', dict(blogs2=blogs2))

def detaille(request,blog_id):
    blogs4 = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'detaille.html', dict(blogs4=blogs4))
