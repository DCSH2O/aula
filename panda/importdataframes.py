import pandas as pd

dados = pd.read_csv('dados_ficticios.csv')

df = pd.DataFrame(data=dados)
print("Idade igual")
print(df[df['idade'] == 46])

print("Renda maior igual a 10 mil")
print(df[df['renda'] >= 10000.00])
