from django.shortcuts import render
from .models import Blog

# Create your views here.


def indexHTML(request):
    return render(request, 'main/index.html')


def blog_view(request):
    queryset = Blog.objects.all()
    context = {
        'objects': queryset
    }
    return render(request, 'main/blog.html', context)


def blog_detail(request, slug):
    blog = Blog.objects.filter(slug=slug)
    context = {
        'blog': blog
    }
    return render(request, 'main/single.html', context)
