'''
from pkg.mod_1 import func_1, func_2
from pkg.mod_2 import func_3, func_4

print(func_1())
print(func_2())
print(func_3())
print(func_4())
'''

import pkg
print(pkg.URL)
'''
Paython indica que el uso de 'namespaces' es una buena practica.
Esto permite evitar problema con elementos de mismo nombre que vengan en distintos paquetes.

Este es un ejemplo de 'namespace' (referencia completa a la función 'func_1')
Para que funcione, primero debe ser importado 'mod_1' desde el archivo '__init__.py'
'''
print(pkg.mod_1.func_1())