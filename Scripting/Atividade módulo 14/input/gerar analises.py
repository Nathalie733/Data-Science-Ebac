import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import os
import sys


sns.set_theme()

def plota_pivot_table(df, value, index, func, ylabel, xlabel, opcao='nada'):
    if opcao == 'nada':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).plot(figsize=[15, 5])
    elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).sort_values(value).plot(figsize=[15, 5])
    elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).unstack().plot(figsize=[15, 5])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    return None


meses = sys.argv[1:]

for mes in meses:
    sinasc = pd.read_csv('SINASC_RO_2019_' + mes + '.csv')

    max_data = sinasc.DTNASC.max()[:7]
    print(max_data)

    output_dir = './output/figs/' + max_data
    os.makedirs(output_dir, exist_ok=True)

    plota_pivot_table(sinasc, 'IDADEMAE', ['DTNASC', 'SEXO'], 'mean', 'media idade mae', 'data de nascimento', 'unstack')
    plt.savefig(os.path.join(output_dir, 'media idade mae por sexo.png'))

    plota_pivot_table(sinasc, 'PESO', ['DTNASC', 'SEXO'], 'mean', 'media peso bebe', 'data de nascimento', 'unstack')
    plt.savefig(os.path.join(output_dir, 'media peso bebe por sexo.png'))

    plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median', 'apgar1 medio', 'gestacao', 'sort')
    plt.savefig(os.path.join(output_dir, 'media apgar1 por escolaridade mae.png'))

    plota_pivot_table(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'apgar1 medio', 'gestacao', 'sort')
    plt.savefig(os.path.join(output_dir, 'media apgar1 por gestacao.png'))

    plota_pivot_table(sinasc, 'APGAR5', 'GESTACAO', 'mean', 'apgar5 medio', 'gestacao', 'sort')
    plt.savefig(os.path.join(output_dir, 'media apgar5 por gestacao.png'))

    plt.close('all')  
