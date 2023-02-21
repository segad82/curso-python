set_countries = {'col', 'mex', 'clp'}

#Podemos identificar la cantidad de elementos en un conjunto.
size = len(set_countries)
print(size) # 3

#Podemos consultar por un elemento en específico.
print('col' in set_countries) # True
print('arg' in set_countries) # False

#Podemos agregar elementos al conjunto.
set_countries.add('arg')
print(set_countries) # {'clp', 'col', 'mex', 'arg'}

#Al agregar un elemento existente, mantiene la regla de NO elementos duplicados.
set_countries.add('col')
print(set_countries) # {'clp', 'col', 'mex', 'arg'}

#Podemos actualizar un conjunto (agrega elementos) sin elementos duplicados.
set_countries.update({'pe', 'ecua', 'clp'})
print(set_countries) # {'ecua', 'col', 'mex', 'clp', 'arg', 'pe'}

#Podemos eliminar un elemento del conjunto.
set_countries.remove('pe')
print(set_countries) # {'mex', 'arg', 'col', 'clp', 'ecua'}

#Cuando tratamos de eliminar un elemento que no existe, python muestra un error.
#set_countries.remove('br')

#Podemos descartar un elemento del conjunto (lo elimina y caso de no existir, el programa no se cae).
set_countries.discard('br')
print(set_countries) # {'mex', 'arg', 'clp', 'col', 'ecua'}
set_countries.discard('ecua')
print(set_countries) # {'mex', 'arg', 'clp', 'col'}

#Podemos limpiar el conjunto eliminando todos los elementos.
set_countries.clear()
print(set_countries) # set()
print(len(set_countries)) # 0