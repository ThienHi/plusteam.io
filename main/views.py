from django.shortcuts import render, get_object_or_404
from .models import Blog, Category
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.


def indexHTML(request):
    return render(request, 'main/index.html')


def blog_view(request):
    queryset = Blog.objects.all()[:3]
    context = {
        'objects': queryset
    }
    return render(request, 'main/blog.html', context)

@api_view(['GET'])
def blog_detail(request, slug):
    blog = Blog.objects.filter(slug=slug)
    all_blog = Blog.objects.all()[:3]
    category = Category.objects.all()
    context = {
        'blog': blog,
        'all': all_blog,
        'category': category
    }
    return render(request, 'main/single.html',context)


def category(request, type, condition):
    list_category = Category.objects.all()

    if type == 'category':
        try:
            category = get_object_or_404(Category, slug = condition)
        except Exception :
            condition = -1
        list_item = Blog.objects.filter(category=category)

    context = {
        'item': list_item,
        'category': list_category
    }
    
    return render(request, 'main/category.html', context)
