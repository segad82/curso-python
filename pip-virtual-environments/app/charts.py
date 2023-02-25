import matplotlib.pyplot as plot

def generate_bar_chart(name, labels, values):
    fig, ax = plot.subplots()
    ax.bar(labels, values)
    plot.savefig(f'./imgs/{name.lower()}.png')
    plot.close()

def generate_pie_chart(labels, values):
    fig, ax = plot.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plot.savefig('./imgs/pie.png')
    plot.close()
    x = 'skbsdlfsfd'