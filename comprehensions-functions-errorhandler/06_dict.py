import random

countries = ['clo', 'clp', 'mex', 'arg']
population = { country: random.randint(1,100) for country in countries }
print(population) # {'clo': 20, 'clp': 21, 'mex': 17, 'arg': 43}
result = { country: quantity for (country, quantity) in population.items() if quantity > 20 }
print(result) # {'clp': 21, 'arg': 43}

texto = 'Hola, mi nombre es Kevin'
print(texto) # Hola, mi nombre es Kevin
unique = { c: c.upper() for c in texto if c in 'aeiou' }
print(unique) # {'o': 'O', 'a': 'A', 'i': 'I', 'e': 'E'}


#        DIFERENCIAS ENTRE LISTAS, TUPLAS Y CONJUNTOS
#-----------------------------------------------------------
#          |  Mutable  |  Ordenada  |  Indexing  |  Duplicar
#          |           |            |  /Slicing  |  Elementos
#-----------------------------------------------------------
#[list]    |    Si     |     Si     |     Si     |     Si
#(tuple)   |    No     |     Si     |     Si     |     Si
#{set}     |    Si     |     No     |     No     |     No