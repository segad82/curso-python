from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.
# Las Function Based Views siempre traen como parámetro un HttpRequest
def index(request):
    latest_question_list = Question.objects.all()
    return render(request, 'polls/index.html', {
        'latest_question_list': latest_question_list
    })

# En python es buena práctica dejar dos espacios en blanco entre funciones
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {
        'question': question
    })


def result(request, question_id):
    return HttpResponse(f"Estás viendo los resultados de la pregunta número {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Estás votando a la pregunta número {question_id}")