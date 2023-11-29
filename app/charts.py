import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title(f'Population of {name} Over Years')
    plt.savefig(f'./imgs/{name}.png')
    plt.close()
