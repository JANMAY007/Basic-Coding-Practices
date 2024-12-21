class Point:

    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")
        return


point = Point(1, 2)
point.z = 10
point.draw()
print(type(point))
print(point.default_color)
print(Point.default_color)
another = Point(3, 4)
another.draw()
