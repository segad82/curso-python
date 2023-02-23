import sys # Elementos sobre el sistema operativo
print(sys.path)

import re # Utilidad para manejar expresiones regulares
text = 'Mi número de teléfono es 0123456789, el código de país es 56, mi número de suerte es 5'
result = re.findall('[0-9]+', text)
print(result) # ['0123456789', '56', '5']

import time # Utilidad para manejar hora y fecha
tiemstamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(tiemstamp) # 1677157743.457256
print(result) # Thu Feb 23 10:09:03 2023

import collections # Utilidad para manejar listas
numbers = [1,1,2,1,2,1,4,5,3,3,21]
counter = collections.Counter(numbers)
# Retorna un diccionario con la frecuencia en la que se repite cada elemento de la lista.
print(counter) # Counter({1: 4, 2: 2, 3: 2, 4: 1, 5: 1, 21: 1})