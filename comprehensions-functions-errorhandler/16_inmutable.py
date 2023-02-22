'''
Los diccionarios a diferencia de las listas, tuplas y conjuntos.
Al crear un nuevo diccionario y modificar sus valores, también modifica el valor de la referencia al diccionario original, haciendo el diccionario mutable.
Este problema se soluciona de la siguiente manera, haciendolo inmutable.
'''
items = [
    { 'product': 'camisa', 'price': 100 },
    { 'product': 'pantalones', 'price': 300 },
    { 'product': 'chaqueta', 'price': 200 }
]

def new_add_taxes(item):
    #Al momento de modificarlo, se debe crear una copia en memoria del elemento original.
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * 0.19
    return new_item

new_items = list(map(new_add_taxes, items))
print(items)
#Aquí se puede ver que no modificó el diccionario original.
'''
[
    {'product': 'camisa', 'price': 100}, 
    {'product': 'pantalones', 'price': 300}, 
    {'product': 'chaqueta', 'price': 200}
]
'''
print(new_items)
'''
[
    {'product': 'camisa', 'price': 100, 'taxes': 19.0}, 
    {'product': 'pantalones', 'price': 300, 'taxes': 57.0}, 
    {'product': 'chaqueta', 'price': 200, 'taxes': 38.0}
]
'''