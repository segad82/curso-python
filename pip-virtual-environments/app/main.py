import pandas as pd
import utils
import charts
from read_csv import read_csv

def run():

    '''
    data = read_csv('data.csv')
    data = list(filter(lambda element : element['Continent'] == 'South America', data))
    countries = list(map(lambda element : element['Country/Territory'], data))
    values = list(map(lambda element : float(element['World Population Percentage']), data))
    '''

    dataframe = pd.read_csv('data.csv')

    data = dataframe[dataframe['Continent'] == 'South America']
    countries = data['Country/Territory'].values
    values = data['World Population Percentage'].values

    charts.generate_pie_chart(countries, values)

    data = read_csv('data.csv')

    country = input('Type Country => ')
    result = utils.population_by_country(data, country)
    if len(result) > 0:
        keys, values = utils.get_population(result[0])
        charts.generate_bar_chart(country, keys, values)

if __name__ == '__main__':
    run()