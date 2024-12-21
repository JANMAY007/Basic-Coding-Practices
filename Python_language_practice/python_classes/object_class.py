class Animal:
    def __init__(self):
        self.age = 1

    @staticmethod
    def eat():
        return "eat"


class Mammal(Animal):
    @staticmethod
    def walk():
        return "walk"


class Fish(Animal):
    @staticmethod
    def swim():
        return "swim"


m = Mammal()
print(isinstance(m, Animal))
print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))
