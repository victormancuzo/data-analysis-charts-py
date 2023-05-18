import pandas as pd
tabela = pd.read_csv("clientes.csv", encoding="latin", sep=";")
print(tabela)


tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors="coerce")
tabela = tabela.dropna()
print(tabela.info())

print(tabela.describe())

import plotly.express as px
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, y="Nota (1-100)", histfunc="avg", text_auto=True, nbins=10)
    grafico.show()