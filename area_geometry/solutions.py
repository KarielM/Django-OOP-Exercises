class Geometry_Area:
    def __init__(self, area):
        self.valid_area = area

    def valid_area(self):
        if self.area < 0:
            raise ValueError

class Square(Geometry_Area):
    def __init__(self, width):
        self.area = width * width

class Triangle(Geometry_Area):
    def __init__(self, base, height):
        self.area = ((base/2) * height)

class Rectangle(Geometry_Area):
    def __init__(self, length, width):
        self.area = length * width