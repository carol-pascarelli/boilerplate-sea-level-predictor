import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Ler dados do arquivo
    data = pd.read_csv('epa-sea-level.csv')

    # Criar gráfico de dispersão
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])

    # Criar a primeira linha de melhor ajuste
    line_A = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    x_values = np.arange(data['Year'].min(), 2051, 1)
    y_values = line_A.slope * x_values + line_A.intercept
    plt.plot(x_values, y_values, label='Line of Best Fit')  # Alterado para o inglês

    # Criar a segunda linha de melhor ajuste para dados a partir de 2000
    data2000 = data[data['Year'] >= 2000]
    line_B = linregress(data2000['Year'], data2000['CSIRO Adjusted Sea Level'])
    x_values_2000 = np.arange(2000, 2051, 1)
    y_values_2000 = line_B.slope * x_values_2000 + line_B.intercept
    plt.plot(x_values_2000, y_values_2000, label='Line of Best Fit (2000-2021)')  # Alterado para o inglês

    # Adicionar rótulos e título
    plt.xlabel('Year')  # Alterado para o inglês
    plt.ylabel('Sea Level (inches)')  # Manter em inglês para evitar falhas
    plt.title('Rise in Sea Level')  # Alterado para o inglês
    plt.legend()

    # Salvar gráfico e retornar dados para teste (NÃO MODIFICAR)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
