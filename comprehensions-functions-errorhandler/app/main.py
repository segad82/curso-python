import utils

data = [
    { 'country': 'Colombia', 'population': 400 },
    { 'country': 'Chile', 'population': 300 }
]

def run():
    keys, values = utils.get_population()
    print(keys, values) # ['col', 'clp'] [400, 300]

    result = utils.population_by_country(data, 'Colombia')
    print(result) # [{'country': 'Colombia', 'population': 400}]

    country = input('Type Country => ')
    result = utils.population_by_country(data, country)
    print(result)

'''
Si este archivo es ejecutado desde la terminal, ejecute esta condición.
Si este archivo es ejecutado desde otro archivo, no ejecute esta condición.
'''
if __name__ == '__main__':
    run()