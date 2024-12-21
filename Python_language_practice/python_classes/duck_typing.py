from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox:
    @staticmethod
    def draw():
        print("text box")


class DropDownList:
    @staticmethod
    def draw():
        print("drop down list")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
# print(isinstance(ddl, UIControl))
tb = TextBox()
draw([ddl, tb])
# polymorphism achieved without inheritance is duck type
