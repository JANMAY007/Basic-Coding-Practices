# class is a blueprint for creating a object
# object is a instance of a class

class Point:

    @staticmethod
    def draw():
        print("inside draw")
        return


point = Point()
point.draw()
print(type(point))
