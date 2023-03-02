from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice

# Create your views here.
# Las Function Based Views siempre traen como parámetro un HttpRequest
#def index(request):
#    latest_question_list = Question.objects.all()
#    return render(request, 'polls/index.html', {
#        'latest_question_list': latest_question_list
#    })

# En python es buena práctica dejar dos espacios en blanco entre funciones
#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/detail.html', {
#        'question': question
#    })


#def result(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#    return render(request, 'polls/result.html', {
#        'question': question
#    })

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # Retornar los últimos 5 elementos publicados
        return Question.objects.order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Seleccione una opción válida"
        })
    else:
        choice.votes += 1
        choice.save()
        '''
        HttpResponseRedirect a diferencia de HttpResponse, se asegura 
        que el usuario no envíe una solicitud más de una vez por error.
        '''
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))
        