from django.shortcuts import render
from .models import Question, Choice
# from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse


def hire(request):
    ques = Question.objects.all()
    paginator = Paginator(ques, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    try:
        contacts = paginator.page(page_number)
        contacts.number = contacts.number +1
        # q = Question.objects.get(pk=contacts.number)
        # data =request.POST["choice"]
        # vote = q.choice_set.get(pk=data)
        # vote.vote = vote.vote + 1
        # vote.save()
    except PageNotAnInteger:
        # Nếu page_number ko thuộc kiểu Integer thì trả về page đầu tiên
        contacts = paginator.page(1)
    except EmptyPage:
        # Nếu page ko có item thì trả về page cuối cùng
        contacts = paginator.page(paginator.num_pages)

    
    context = {
        'q':ques,
        'page':contacts,
        'page_number': page_obj
    }
    return render(request,'hire/hire.html',context)


def vote(request, question_id):
    q = Question.objects.get(pk=question_id)
    try:
        data = request.POST["choice"]
        c = q.choice_set.get(pk=data)
    except:
        HttpResponse("Error exits data")
    c.vote = c.vote + 1
    c.save()
    return render(request, "hire/vote.html", {"vote": q})