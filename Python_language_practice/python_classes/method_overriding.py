class Animal:
    def __init__(self):
        print("Animal class constructor")
        self.age = 1

    @staticmethod
    def eat():
        return "eat"


class Mammal(Animal):
    def __init__(self):
        super(Mammal, self).__init__()
        print("Mammal class constructor")
        self.weight = 10

    @staticmethod
    def walk():
        return "walk"


class Fish(Animal):
    @staticmethod
    def swim():
        return "swim"


m = Mammal()
print(m.age)
print(m.weight)
