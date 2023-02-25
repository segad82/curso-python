import matplotlib.pyplot as plot
import random

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [ random.randint(1, 100) for i in range(0,3)]
    fig, ax = plot.subplots()
    ax.pie(values, labels=labels)
    plot.savefig('pie.png')
    plot.close()