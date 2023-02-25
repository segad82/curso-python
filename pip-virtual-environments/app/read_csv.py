import csv

def read_csv(path):
    with open(path) as file:
        reader = csv.reader(file, delimiter=',')
        titles = list(next(reader))
        data = []
        for row in reader:
            #result = dict(zip(titles, row))
            iterable = list(zip(titles, row))
            dictionary = { key : value for (key, value) in iterable } # dictionary comprehension
            data.append(dictionary)
        return data

if __name__ == '__main__':
    result = read_csv('./app/data.csv')
    print (result)