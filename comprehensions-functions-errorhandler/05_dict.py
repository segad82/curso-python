numbers = {}
for i in range(1,5):
    numbers[i] = i * 2
print(numbers)

#Dictionario Comprehension sirve para generar diccionarios en una línea de código.
numbers = { i: i * 2 for i in range(1,5) }
print(numbers)

import random

countries = ['col', 'clp', 'arg']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
print(population)

population = { country: random.randint(1, 100) for country in countries }
print(population)

people = ['juan', 'pablo', 'pedro']
ages = [20, 25, 23]

#La función 'zip' sirve para unir dos listas.
print(list(zip(people, ages)))

result = {}
for (name, age) in zip(people, ages):
    result[name] = age
print(result)

result = { name: age for (name, age) in zip(people, ages) }
print(result)

#Otra forma que descubrí cómo llegar al mismo resultado es la siguiente.
print(dict(zip(people, ages)))
