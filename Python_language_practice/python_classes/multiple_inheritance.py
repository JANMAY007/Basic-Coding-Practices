class Positive:
    @staticmethod
    def good():
        return "plus"


class Negative:
    @staticmethod
    def bad():
        return "minus"


class Neutral:
    @staticmethod
    def neutral():
        return "zero"


class Human(Positive, Negative, Neutral):
    pass


human = Human()
print(human.good())
print(human.bad())
print(human.neutral())
