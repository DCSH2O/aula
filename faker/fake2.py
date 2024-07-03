import csv
from faker import Faker

def criar_personas(quantidade):
    fake = Faker('pt_BR')
    personas = []
    for _ in range(quantidade):
        persona = {
            'Nome': fake.name(),
            'Cidade': fake.city(),
            'Idade': fake.random_int(min=18, max=80)
        }
        personas.append(persona)
    return personas

def salvar_personas_csv(personas, nome_arquivo):
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Nome', 'Cidade', 'Idade'])
        writer.writeheader()
        writer.writerows(personas)

if __name__=='__main__':
    quantidade_personas = 10  # Defina a quantidade de personas a serem criadas
    personas = criar_personas(quantidade_personas)
    salvar_personas_csv(personas, 'personas.csv')
    print(f'{quantidade_personas} personas foram salvas no arquivo personas.csv.')