from django.urls import path
from . import views

urlpatterns = [
    # ex: ~/polls/ => Estás en la página principal de Premios Platzi App
    path('', views.index, name='index'),
    # ex: ~/polls/2/ => Estás viendo la pregunta número 2
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: ~/polls/3/result => Estás viendo los resultados de la pregunta número 3
    path('<int:question_id>/result', views.result, name='result'),
    # ex: ~/polls/4/vote => Estás votando a la pregunta número 4
    path('<int:question_id>/vote', views.vote, name='vote'),
]