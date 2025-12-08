class TwoDimShape(object):
    def __init__(self):
        pass

    def area(self):
        pass


class ThreeDimShape(TwoDimShape):
    def __init__(self):
        pass

    def volume(self):
        pass

class square(TwoDimShape):
    def __init__(self, x, y, edge):
        self.top_left_x = x
        self.top_left_y = y
        self.edge = edge

    def area(self):
        return self.edge ** 2

    def __str__(self):
        return f"square[ x: {self.top_left_x}, y: {self.top_left_y} , edge: {self.edge}  ]"


class cube(ThreeDimShape):
    def __init__(self, x, y, z, edge):
        self.x = x
        self.y = y
        self.z = z
        self.edge = edge

    def area(self):
        return 6.0 * self.edge ** 2

    def volume(self):
        return self.edge ** 3

    def __str__(self):
        return f"cube[ x: {self.x}, y: {self.y} , z: {self.z}, edge: {self.edge}  ]"

shapes : [TwoDimShape] = [
    square(100, 200, 100),
    square(200, 300, 200),
    square(300, 400, 300),
    cube(100, 200, 100, 2),
]
print(dir(shapes[0]))
for shape in shapes:
    print(shape, shape.area())
    #if "volume" in dir(shape):
    if isinstance(shape,ThreeDimShape):
        print(shape.volume())
