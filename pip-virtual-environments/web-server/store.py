import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code) # 200
    print(r.text) # Lista de categorías
    print(type(r.text)) # <class 'str'>
    categories = r.json() # Convierte la lista de categorías a un formato que reconoce python para poder iterar
    [ print(category['name']) for category in categories ]