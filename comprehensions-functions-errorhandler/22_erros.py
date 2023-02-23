#Los error se pueden manejar mediante el try/except de la siguiente manera.

try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)

try:
    assert 1 != 1, 'Uno no es igual a uno'
except AssertionError as error:
    print(error)

try:
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad')
except Exception as error:
    print(error)

print('*' * 30)
#Se puede unificar el códifo anterior de la siguiente manera y manejar cada uno de los errores.

try:
    print(0/0)
    
    assert 1 != 1, 'Uno no es igual a uno'

    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)

print('El programa continua sin caerse')