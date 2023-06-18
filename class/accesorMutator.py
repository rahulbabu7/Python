#!program to show the mutator and accessor in python class
class Person:
    def __init__(self, name):
        self.name = name
    
    #!ACCESSOR METHOD
    def get_name(self):
        return self.name

    
    #!MUTATOR METHOD
    def set_name(self, new_name):
        self.name = new_name

person = Person("John")
person.set_name("Jane")
print(person.get_name())  # Output: Jane
