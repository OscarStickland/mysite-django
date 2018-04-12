from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request, 'index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    responce = "You're looking at the results of question %s."
    return HttpResponse(responce % question_id)

def vote(request, question_id):
    return HttpResponse("Your voting on question %s." % question_id)


