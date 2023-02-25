import re

def get_population(data):
    result = { key[:4] : value for key, value in data.items() if re.findall('[0-9]+ Population', key) }
    keys = [ key for key in result.keys() ]
    values = [ int(value) for value in result.values() ]
    return keys, values

def population_by_country(data, country):
    result = list(filter(lambda item : item['Country/Territory'] == country, data))
    return result