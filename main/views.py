from django.shortcuts import render, get_object_or_404
from .models import Blog, Category, Email
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
# from django.core.mail import send_mail
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .forms import EmailForms
from django.conf import settings

def indexHTML(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        content = request.POST.get('content')
        html_content = render_to_string('main/send.html', {'email':email,'content': content})
        text_content = strip_tags(html_content)
        emails = EmailMultiAlternatives(
            "Test Subject",
            content,
            settings.EMAIL_HOST_USER,
            ['5951071101@st.utc2.edu.vn'],
        )
        emails.attach_alternative(html_content,'text/html')
        emails.send()
        # return render(request, 'main/index.html')
    return render(request, 'main/index.html')


# def send(request):
#     # email = EmailForms()
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         subject = request.POST.get('subject')
#         email = request.POST.get('email')
#         content = request.POST.get('content')
#         send_mail(
#             subject,
#             content,
#             email,
#             ['yovalip420@cnxingye.com']
#         )

#     return render(request, 'main/index.html')



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
