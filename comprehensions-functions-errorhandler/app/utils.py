def get_population():
    keys = ['col', 'clp']
    values = [400, 300]
    return keys, values

def population_by_country(data, country):
    result = list(filter(lambda item : item['country'] == country, data))
    return result