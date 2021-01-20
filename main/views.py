from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.


def indexHTML(request):
    return render(request, 'main/index.html')


def blog_view(request):
    queryset = Blog.objects.all()
    context = {
        'objects': queryset
    }
    return render(request, 'main/blog.html', context)

@api_view(['GET'])
def blog_detail(request, slug):
    blog = Blog.objects.filter(slug=slug)
    all_blog = Blog.objects.all()
    context = {
        'blog': blog,
        'all': all_blog
    }
    return render(request, 'main/single.html',context)
