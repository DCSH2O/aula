print("Teste Virtual")
# comando para criar ambiente virtual
# python -m venv env
# .\env\Scripts\activate
# codigo para forcar mudança nas politicas do windows
# Set-ExecutionPolicy Unrestricted -Force 
# pip install virtualenv
# virtualenv nome_do_ambiente(pasta)

import requests
import json


# Estrutura do dicionário com nome e CEP de cada integrante..
squad = [
    {"nome": "", "cep": ""},
    {"nome": "", "cep": ""},
]

def consultar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Solicitar ao usuário os nomes e CEPs para cada integrante
for integrante in squad:
    integrante["nome"] = input(f'Digite o nome do integrante {integrante["nome"]}: ')
    integrante["cep"] = input(f'Digite o CEP para integrante {integrante["nome"]}: ')

# Consultar e imprimir nome e cidade de cada integrante
for integrante in squad:
    dados = consultar_cep(integrante["cep"])
    if dados:
        print(f'Nome: {integrante["nome"]}, Cidade: {dados["localidade"]}')
    else:
        print(f'Erro ao consultar CEP de {integrante["nome"]}')