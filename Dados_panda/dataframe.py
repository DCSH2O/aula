import pandas as pd

# Dados
data = {
    'Nome': ['Dione Braga', 'Diony', 'Maria', 'João', 'Luiza', 'Carlos', 'Mariana'],
    'Idade': [25, 30, 28, 35, 27, 32, 29],
    'Cidade': ['Recife', 'Recife', 'Recife', 'Salvador', 'Salvador', 'São Paulo', 'Manaus']
}

# Criar DataFrame
df = pd.DataFrame(data)

# Filtrar moradores do Recife
recife_df = df.loc[df['Cidade'] == 'Recife']
# Filtrar moradores do salvador
salvador_df = df.loc[df['Cidade'] == 'Salvador']

idade_df = df.loc[df['Idade'] >= 30]

# Exibir o DataFrame filtrado

# Recife
print("Moradores do Recife:")
print(recife_df)
# Salvador
print("Moradores do Salvador:")
print(salvador_df)

print("Moradores idade maior igual que 30:")
print(idade_df)