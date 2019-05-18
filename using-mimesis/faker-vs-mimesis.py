import cProfile

from mimesis import Person
from faker import Faker

person = Person()
faker = Faker()

# Generating using Mimesis:
cProfile.run('[person.full_name() for _ in range(10000)]')

# Generating using Faker:
cProfile.run('[faker.name() for _ in range(10000)]')
