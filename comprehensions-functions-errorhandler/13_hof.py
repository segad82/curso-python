#Higher order function (HOF)

#Podemos agregar funciones como parámetro dentro de otra función.
def increment(x):
    return x + 1

def hof(x, func):
    return x + func(x)

result = hof(1, increment) # 1 + 1 + 1
print(result) # 3

result = hof(5, increment) # 5 + 5 + 1
print(result) # 11


#Podemos hacer lo mismo con expresiones lambda.
increment_v2 = lambda x : x + 1
hot_v2 = lambda x, func: x + func(x)

result = hot_v2(3, increment_v2) # 3 + 3 + 1
print(result) # 7

#Podemos incluso definir una función lambda directamente como parámetro en otra función.
result = hot_v2(4, lambda x : x + 2) # 4 + 4 + 2
print(result) # 10