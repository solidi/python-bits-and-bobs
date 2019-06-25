class ClassWithoutSlots(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier


class ClassWithSlots(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
    
    def __repr__(self):
        return self.name

b = ClassWithSlots("Doug", "Human")
print(b)