items = [
    { 'product': 'camisa', 'price': 100 },
    { 'product': 'pantalones', 'price': 300 },
    { 'product': 'chaqueta', 'price': 200 }
]

result = list(map(lambda item : item['price'], items))
print(result) # [100, 300, 200]

def add_taxes(item):
    item['taxes'] = item['price'] * 0.19
    return item

new_items = list(map(add_taxes, items))
print(items)
#¿Porqué modifica el diccionario original?
'''
[
    {'product': 'camisa', 'price': 100, 'taxes': 19.0}, 
    {'product': 'pantalones', 'price': 300, 'taxes': 57.0}, 
    {'product': 'chaqueta', 'price': 200, 'taxes': 38.0}
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