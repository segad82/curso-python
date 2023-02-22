numbers = {}
for i in range(1,5):
    numbers[i] = i * 2
print(numbers) # {1: 2, 2: 4, 3: 6, 4: 8}

#Dictionario Comprehension sirve para generar diccionarios en una línea de código.
numbers = { i: i * 2 for i in range(1,5) }
print(numbers) # {1: 2, 2: 4, 3: 6, 4: 8}

import random

countries = ['col', 'clp', 'arg']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
print(population) # {'col': 18, 'clp': 32, 'arg': 74}

population = { country: random.randint(1, 100) for country in countries }
print(population) # {'col': 94, 'clp': 29, 'arg': 55}

people = ['juan', 'pablo', 'pedro']
ages = [20, 25, 23]

#La función 'zip' sirve para unir dos listas.
print(list(zip(people, ages))) # [('juan', 20), ('pablo', 25), ('pedro', 23)]

result = {}
for (name, age) in zip(people, ages):
    result[name] = age
print(result) # {'juan': 20, 'pablo': 25, 'pedro': 23}

result = { name: age for (name, age) in zip(people, ages) }
print(result) # {'juan': 20, 'pablo': 25, 'pedro': 23}

#Otra forma que descubrí cómo llegar al mismo resultado es la siguiente.
print(dict(zip(people, ages))) # {'juan': 20, 'pablo': 25, 'pedro': 23}
