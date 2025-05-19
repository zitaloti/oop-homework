import math
from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def get_dimension(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    def lateral_area(self):
        raise NotImplementedError("Lateral area not applicable")

    def base_area(self):
        raise NotImplementedError("Base area not applicable")

    def get_height(self):
        raise NotImplementedError("Height not applicable")

    @abstractmethod
    def measure(self):
        pass

class FlatFigure(Figure):
    def get_dimension(self):
        return 2

    def lateral_area(self):
        raise NotImplementedError("Lateral area not defined for 2D")

    def base_area(self):
        raise NotImplementedError("Base area not defined for 2D")

    def get_height(self):
        raise NotImplementedError("Height not defined for 2D")

    def measure(self):
        return self.get_area()

class SolidFigure(Figure):
    def get_dimension(self):
        return 3

    def get_perimeter(self):
        raise NotImplementedError("Perimeter not defined for 3D")

    def get_area(self):
        raise NotImplementedError("Area not defined for 3D")

class Triangle(FlatFigure):
    def __init__(self, x, y, z):
        self.edges = sorted([x, y, z])
        if self.edges[0] + self.edges[1] <= self.edges[2]:
            raise ValueError("Not a valid triangle")

    def get_perimeter(self):
        return sum(self.edges)

    def get_area(self):
        s = self.get_perimeter() / 2
        a, b, c = self.edges
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Rectangle(FlatFigure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width

class Trapezoid(FlatFigure):
    def __init__(self, base1, base2, side1, side2):
        self.base1 = base1
        self.base2 = base2
        self.side1 = side1
        self.side2 = side2

    def get_perimeter(self):
        return self.base1 + self.base2 + self.side1 + self.side2

    def get_area(self):
        mid = abs(self.base2 - self.base1) / 2
        discriminant = self.side1**2 - mid**2
        if discriminant < 0:
            raise ValueError("Invalid trapezoid dimensions")
        height = math.sqrt(discriminant)
        return (self.base1 + self.base2) * height / 2

class Parallelogram(FlatFigure):
    def __init__(self, base, side, height):
        self.base = base
        self.side = side
        self.h = height

    def get_perimeter(self):
        return 2 * (self.base + self.side)

    def get_area(self):
        return self.base * self.h

class Circle(FlatFigure):
    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * self.radius ** 2

class Sphere(SolidFigure):
    def __init__(self, radius):
        self.radius = radius

    def lateral_area(self):
        return 4 * math.pi * self.radius ** 2

    def measure(self):
        return (4/3) * math.pi * self.radius ** 3

class EquilateralPyramid(Triangle, SolidFigure):
    def __init__(self, edge, height):
        Triangle.__init__(self, edge, edge, edge)
        self.h = height

    def lateral_area(self):
        l = math.sqrt(self.h**2 + (self.edges[0] * math.sqrt(3) / 6)**2)
        return 3 * self.edges[0] * l / 2

    def measure(self):
        return Triangle.get_area(self) * self.h / 3

class RectPyramid(Rectangle, SolidFigure):
    def __init__(self, a, b, height):
        Rectangle.__init__(self, a, b)
        self.h = height

    def lateral_area(self):
        l1 = math.sqrt((self.length/2)**2 + self.h**2)
        l2 = math.sqrt((self.width/2)**2 + self.h**2)
        return self.length * l2 + self.width * l1

    def measure(self):
        return self.get_area() * self.h / 3

class Box(Rectangle, SolidFigure):
    def __init__(self, a, b, c):
        Rectangle.__init__(self, a, b)
        self.c = c

    def lateral_area(self):
        return 2 * (self.length*self.width + self.width*self.c + self.length*self.c)

    def measure(self):
        return self.length * self.width * self.c

class Cone(Circle, SolidFigure):
    def __init__(self, radius, height):
        Circle.__init__(self, radius)
        self.h = height

    def lateral_area(self):
        slant = math.sqrt(self.radius ** 2 + self.h ** 2)
        return math.pi * self.radius * slant

    def measure(self):
        return Circle.get_area(self) * self.h / 3

class TriangularPrism(Triangle, SolidFigure):
    def __init__(self, a, b, c, height):
        Triangle.__init__(self, a, b, c)
        self.h = height

    def lateral_area(self):
        return self.get_perimeter() * self.h + 2 * self.get_area()

    def measure(self):
        return self.get_area() * self.h

def parse_figure(description):
    parts = description.split()
    type_ = parts[0]
    nums = list(map(float, parts[1:]))

    match type_:
        case "Triangle": return Triangle(*nums)
        case "Rectangle": return Rectangle(*nums[:2])
        case "Trapeze": return Trapezoid(*nums)
        case "Parallelogram": return Parallelogram(*nums)
        case "Circle": return Circle(nums[0])
        case "Ball": return Sphere(nums[0])
        case "TriangularPyramid": return EquilateralPyramid(*nums)
        case "QuadrangularPyramid": return RectPyramid(*nums)
        case "RectangularParallelepiped": return Box(*nums)
        case "Cone": return Cone(*nums)
        case "TriangularPrism": return TriangularPrism(*nums)
        case _: return None

def max_measure_shape(figures):
    return max(figures, key=lambda f: f.measure())

def run_on_file(path):
    items = []
    with open(path) as f:
        for row in f:
            try:
                fig = parse_figure(row.strip())
                if fig:
                    items.append(fig)
            except Exception as e:
                print(f"Skipping invalid shape in line: '{row.strip()}' ({e})")
    if items:
        best = max_measure_shape(items)
        print(f"In {path} the shape with the max measure is {best.__class__.__name__}")
        print(f"Measure: {best.measure()}")
    else:
        print(f"No valid shapes in {path}")

if __name__ == "__main__":
    for filename in ["input01.txt", "input02.txt", "input03.txt"]:
        run_on_file(filename)
        print("-" * 40)
