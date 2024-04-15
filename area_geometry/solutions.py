class Geometry_Area:
    def __init__(self, area):
        self.area = area

    def valid_area(self):
        if self.area < 0:
            raise ValueError

class Square(Geometry_Area):
    def __init__(self, width):
        # self.area = width * width
        #area = width ** 2
        #super().__init__(area)
        super().__init__(width ** 2)

class Triangle(Geometry_Area):
    def __init__(self, base, height):
        # self.area = ((base/2) * height)
        super().__init__((base/2)*height)

class Rectangle(Geometry_Area):
    def __init__(self, length, height):
        # self.area = length * height
        super().__init__(length * height)