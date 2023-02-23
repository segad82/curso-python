import utils

keys, values = utils.get_population()
print(keys, values) # ['col', 'clp'] [400, 300]

data = [
    { 'country': 'Colombia', 'population': 400 },
    { 'country': 'Chile', 'population': 300 }
]

result = utils.population_by_country(data, 'Colombia')
print(result) # [{'country': 'Colombia', 'population': 400}]

country = input('Type Country => ')
result = utils.population_by_country(data, country)
print(result)