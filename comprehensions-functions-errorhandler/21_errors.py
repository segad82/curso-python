'''
Error cuando el código está mal escrito.
print(0/0)) # SyntaxError

Error cuando de hacen diviciones entre cero.
#print(0/0) # ZeroDivisionError

Error cuando se hacer referencia a una variable que no existe.
print(result) # NameError

Error cuando no funciona un assert
suma = lambda x,y : x - y
assert suma(2,2) == 4 # AssertionError

Podemos generar exepciones propias de la siguiente manera.
age = 10
if age < 18:
    raise Exception('No se permiten menores de edad') # Exception: [mensaje]
'''