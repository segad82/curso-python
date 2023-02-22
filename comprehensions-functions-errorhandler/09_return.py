#Podemos definir valores por defecto en los parámetros de una función y retornar más de un argumento.
def find_volume(length=1, width=1, depth=1):
    return length * width * depth, width, 'hola'

result, width, text = find_volume(width=10)

print(result) # 10
print(width) # 10
print(text) # hola