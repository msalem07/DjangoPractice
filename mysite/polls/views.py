from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question, Choice
from django.views import generic
#shorcut to loader.get_template
from django.shortcuts import render
from django.utils import timezone
# Create your views here.
#Initial Templates, these are being replaced with the bottom ones 
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     #output = ', '.join([q.question_text for q in latest_question_list])
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     #without shortcut
#     #template = loader.get_template('polls/index.html')
#     #return HttpResponse(template.render(context, request))

#     return render(request, 'polls/index.html', context)

# def detail(request, question_id):

#     #Without shortcut
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exists")

#     #With shortcut
#     question = get_object_or_404(Question, pk=question_id)

#     return render(request, 'polls/details.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

class IndexView(generic.ListView):

    #The context attribute for listView returned becomes the models name in lowercase plus list, in this case question_list. 
    template_name = 'polls/index.html'
    #Override that name and use custom one.'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    #The context attribute returned becomes the models name in lowercase, in this case question.
    #Argument on url needs to now refer to pk instead of question_id
    model = Question
    template_name = 'polls/details.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):

        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        #Use HttpResponseRedirect for forms. Prevents them from being posted twice
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))