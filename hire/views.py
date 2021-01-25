from django.shortcuts import render
from .models import Question, Choice
# from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse


def hire(request):
    ques = Question.objects.all()
    paginator = Paginator(ques, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # print("======================================================================")
    # print(page_obj)

    context = {
        'q':ques,
        'page':page_obj
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