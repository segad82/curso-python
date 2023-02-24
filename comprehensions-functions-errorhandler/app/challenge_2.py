from read_csv import read_csv
from charts import generate_pie_chart

if __name__ == '__main__':
    data = read_csv('./../app/data.csv')
    '''
    # Solución propia. (Me di muchas vueltas haciendo recorridos de más)
    titles = ('Country/Territory', 'World Population Percentage')
    result = list(map(lambda element : { title : element[title] for title in titles }, data))
    countries = [ directory[titles[0]] for directory in result ]
    values = [ float(directory[titles[1]]) for directory in result ]
    generate_pie_chart(countries, values)
    '''
    # Solución del profe.
    data = list(filter(lambda element : element['Continent'] == 'South America', data))
    countries = list(map(lambda element : element['Country/Territory'], data))
    values = list(map(lambda element : float(element['World Population Percentage']), data))
    generate_pie_chart(countries, values)