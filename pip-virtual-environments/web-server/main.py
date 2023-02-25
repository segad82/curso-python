import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,4]

@app.get('/contact')
def get_list():
    return { 'name': 'Platzi' }

@app.get('/web', response_class=HTMLResponse)
def get_list():
    return '''
    <h1>Ejemplo de pagina web</h1>
    <p>Esto es una muestra de como renderizar paginas web con FastAPI.</p>
    '''

def run():
    store.get_categories()

if __name__ == '__main__':
    run()