# the argument of the class name is the parent class inherited in the corresponding class
# like Animal is inherited in the Mammal class and Fish class
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
m.eat()
m.walk()
print(m.age)

f = Fish()
f.eat()
f.swim()
print(f.age)
