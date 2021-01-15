from django.shortcuts import render

# Create your views here.


def indexHTML(request):
    return render(request, 'main/index.html')
