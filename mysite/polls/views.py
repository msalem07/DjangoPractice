from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question

#shorcut to loader.get_template
from django.shortcuts import render


# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    context = {
        'latest_question_list': latest_question_list,
    }
    #without shortcut
    #template = loader.get_template('polls/index.html')
    #return HttpResponse(template.render(context, request))

    return render(request, 'polls/index.html', context)

def detail(request, question_id):

    #Without shortcut
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exists")

    #With shortcut
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/details.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question {}".format(question_id)
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse("You're voting on question {}".format(question_id))