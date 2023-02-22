numbers = []
for element in range(1,11):
    numbers.append(element)
print(numbers)

#List Comprehension sirve para generar listas en una línea de código a través de la siguiente sintaxis.
numbers = [element for element in range(1,11)]
print(numbers)

numbers_v2 = []
for i in range(1,11):
    if i % 2 == 0:
        numbers_v2.append(i*2)
print(numbers_v2)

numbers_v2 = [i * 2 for i in range(1,11) if i % 2 == 0]
print(numbers_v2)
