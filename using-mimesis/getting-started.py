from mimesis import Person
from mimesis.enums import Gender

person = Person('en')
print(person.full_name())
print(person.occupation())
print(person.telephone())

de = Person('de')
en = Person('en')

print(de.full_name(gender=Gender.FEMALE))
print(en.full_name(gender=Gender.MALE))
