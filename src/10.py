from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Creating instances
dog = Dog()
cat = Cat()

print("Dog says:", dog.make_sound())
print("Cat says:", cat.make_sound())
# Output
# Dog says: Bark
# Cat says: Meow