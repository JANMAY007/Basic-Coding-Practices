class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    """def draw(self):
        print(f"Point ({self.x}, {self.y})")
        return"""

    # try to make self of giving first priority than another
    def __eq__(self, another):
        if self.x == another.x and self.y == another.y:
            return True

    def __add__(self, another):
        return Point(self.x + other.x, self.y + other.y)


point = Point(1, 2)
# print(str(point))
other = Point(1, 2)
print(point == other)
print(point + other)
