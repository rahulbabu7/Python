from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class Lion(Animal):
    def eat(self):
        print("Lion eats meat.")

    def sleep(self):
        print("Lion sleeps in its den.")

class Tiger(Animal):
    def eat(self):
        print("Tiger eats meat.")

    def sleep(self):
        print("Tiger sleeps in the forest.")

class Deer(Animal):
    def eat(self):
        print("Deer eats grass.")

    def sleep(self):
        print("Deer sleeps in the meadow.")

# Create instances of the subclasses
lion = Lion()
tiger = Tiger()
deer = Deer()

# Call the eat() and sleep() methods for each animal
lion.eat()
lion.sleep()

tiger.eat()
tiger.sleep()

deer.eat()
deer.sleep()
