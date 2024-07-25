import pandas as pd
import seaborn as sns

df = pd.read_csv('gasolina.csv')
with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=df, x='dia', y='venda')
grafico.set(title='Preço do lt gasolina por dia', xlabel='Dia', ylabel='Preço do litro')
grafico.figure.savefig('gasolina.png')