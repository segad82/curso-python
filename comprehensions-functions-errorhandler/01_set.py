#Los conjuntos en python se representan de la siguiente manera.
#Nota: No confundir con los directorios que tiene clave y valor.
set_countries = {'col', 'mex', 'clp'}
print(set_countries)
print(type(set_countries))

#Los conjuntos no tienen elementos duplicados aunque sean mencionados en su definición.
set_numbers = {1,2,2,443,23}
print(set_numbers)

#Los conjuntos pueden contener distintos tipos de datos.
set_types = {1, 'hola', False, 12.12}
print(set_types)

#Se puede transformar a conjunto, una cadena de caracteres.
#Nótese que mantiene la regla de no contener elementos duplicados.
set_from_string = set('hoola')
print(set_from_string)

#Se puede transormar a conjunto, una tupla.
#También repeta la regla de no eliementos duplicados.
set_from_tuples = set(('abc', 'cbv', 'as,', 'abc'))
print(set_from_tuples)

#Se puede transformar a conjunto, una lista.
numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)

#Se puede transformar un conjunto a una lista.
#Esto es un ejemplo de cuando se quiere extraer los elementos únicos de una lista.
unique_numbers = list(set_numbers)
print(unique_numbers)

#También se puede transformar un conjunto a una tupla.
unique_numbers = tuple(set_numbers)
print(unique_numbers)