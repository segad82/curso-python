#Map sirve para transformar los elementos de una lista/tupla/conjunto de elementos.
#[vaca, pollo, mazorca, papa] -> | cocinar() | -> [hamburguesa, nuggets, palomitas, rizadas]

numbers = [1,2,3,4]
print(numbers) # [1, 2, 3, 4]

result = []
for i in numbers:
    result.append(i * 2)
print(result) # [2, 4, 6, 8]

result = list(map(lambda x : x * 2, numbers))
print(result) # [2, 4, 6, 8]

#Al transformar la unión de dos listas, la función 'map' genera el resultado en base la lista más pequeña.
numbers_v1 = [1,2,3,4]
numbers_v2 = [5,6,7]
result = list(map(lambda x, y : x + y, numbers_v1, numbers_v2))
print(numbers_v1) # [1, 2, 3, 4]
print(numbers_v2) # [5, 6, 7]
print(result) # [6, 8, 10]