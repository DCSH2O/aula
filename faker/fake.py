from faker import Faker

faker = Faker('pt_BR')

print(faker.name())
print(faker.address())