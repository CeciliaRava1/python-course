class MyPerson: # CamelCase
    pass # Null statement
# print(MyPerson())

class Person:
    def __init__(self, name, surname): # Constructor
        self.name = name
        self.surname = surname
    
    def walk(self):
        print(f'{self.name} is walking')

my_person = Person('Ludmila', 'Gutierrez')
print(my_person.name)
my_person.walk()
