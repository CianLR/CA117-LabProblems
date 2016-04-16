class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        return ((self.x - p2.x)**2 + (self.y - p2.y)**2)**0.5


class Shape:
    def __init__(self, points):
        self.points = points

    def sides(self):
        return [self.points[i].distance(self.points[i+1]) for i in range(-1, len(self.points)-1)]

    def perimeter(self):
        return sum(self.sides())


class Triangle(Shape):
    def area(self):
        s = self.perimeter / 2
        a, b, c = self.sides()

        return (s*(s - a)*(s - b)*(s - c))**0.5


class Square(Shape):
    def area(self):
        a, b, _, _ = self.sides()
        return a*b
