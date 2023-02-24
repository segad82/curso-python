from read_csv import read_csv
from charts import generate_bar_chart
import re

if __name__ == '__main__':
    data = read_csv('./../app/data.csv')
    country = 'Colombia'
    rows = list(filter(lambda element : element['Country/Territory'] == country, data))
    if len(rows) > 0:
        result = { key[:4] : value for key, value in rows[0].items() if re.findall('[0-9]+ Population', key) }
        titles = [ key for key in result.keys() ]
        values = [ int(value) for value in result.values() ]
        generate_bar_chart(titles, values)