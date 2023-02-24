'''
[matplotlib] es la librería que permite hacer gráficos fácilmente con python.
Podemos definir alias a una referencia para hacer más fácil su uso.
'''
import matplotlib.pyplot as plot
import random

def generate_bar_chart(labels, values):
    fig, ax = plot.subplots()
    ax.bar(labels, values) # Gráfico de barras
    plot.show()

def generate_pie_chart(labels, values):
    fig, ax = plot.subplots()
    ax.pie(values, labels=labels) # Gráfico de torta
    ax.axis('equal')
    plot.show()

if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [ random.randint(0, 100) for i in range(0, len(labels))]
    #generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)