from django.db import models

# Create your models here.

'''
ORM: Object Relational Mapping
Representación de una base de datos, mediante clases (POO)
Todos los modelos ORM heredan de la clase 'models.Model'
'''
class Question(models.Model):
    # Los campos de tabla se declaran de la siguiente manera:
    #id -> Se puede omitir ya que django lo considera automáticamente.
    question_text = models.CharField(max_length=200) # El parámetro 'max_length' es obligatorio para este tipo de dato.
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    '''
    Mediante la declaración de 'on_delete=models.CASCADE'
    Cada que se elimina una pregunta, elimina en cascada todas las respuestas relacionadas a la pregunta.
    '''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)