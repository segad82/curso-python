from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Las Function Based Views siempre traen como parámetro un HttpRequest
def index(request):
    return HttpResponse('Estás en la página principal de Premios Platzi App')

# En python es buena práctica dejar dos espacios en blanco entre funciones
def detail(request, question_id):
    return HttpResponse(f"Estás viendo la pregunta número {question_id}")


def result(request, question_id):
    return HttpResponse(f"Estás viendo los resultados de la pregunta número {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Estás votando a la pregunta número {question_id}")