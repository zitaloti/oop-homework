import math

class Shape:
    def perimeter(self):
        pass

    def area(self):
        pass

class Triangle(Shape):
    def __init__(self, a, b, c):
        if not self._is_valid_triangle(a, b, c):
            raise ValueError(f"Invalid triangle with sides {a}, {b}, {c}")
        self.a = a
        self.b = b
        self.c = c

    def _is_valid_triangle(self, a, b, c):
        return (a > 0 and b > 0 and c > 0 and
                a + b > c and b + c > a and a + c > b)

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def __str__(self):
        return f"Triangle({self.a}, {self.b}, {self.c})"

class Rectangle(Shape):
    def __init__(self, a, b):
        if a <= 0 or b <= 0:
            raise ValueError(f"Invalid rectangle with sides {a}, {b}")
        self.a = a
        self.b = b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.b

    def __str__(self):
        return f"Rectangle({self.a}, {self.b})"

class Trapeze(Shape):
    def __init__(self, a, b, c, d):
        if a <= 0 or b <= 0 or c <= 0 or d <= 0:
            raise ValueError(f"Invalid trapeze with sides {a}, {b}, {c}, {d}")
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        s = self.perimeter() / 2
        try:
            h = 2 * math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c) * (s - self.d) -
                             (self.a * self.b * self.c * self.d) / 16) / (self.a + self.b)
            return (self.a + self.b) * h / 2
        except (ValueError, ZeroDivisionError):
            raise ValueError(f"Cannot compute area for trapeze with sides {self.a}, {self.b}, {self.c}, {self.d}")

    def __str__(self):
        return f"Trapeze({self.a}, {self.b}, {self.c}, {self.d})"

class Parallelogram(Shape):
    def __init__(self, a, b, h):
        if a <= 0 or b <= 0 or h <= 0:
            raise ValueError(f"Invalid parallelogram with sides {a}, {b}, height {h}")
        self.a = a
        self.b = b
        self.h = h

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a * self.h

    def __str__(self):
        return f"Parallelogram({self.a}, {self.b}, height={self.h})"

class Circle(Shape):
    def __init__(self, r):
        if r <= 0:
            raise ValueError(f"Invalid circle with radius {r}")
        self.r = r

    def perimeter(self):
        return 2 * math.pi * self.r

    def area(self):
        return math.pi * self.r * self.r

    def __str__(self):
        return f"Circle(radius={self.r})"

def create_shape(shape_data):
    try:
        parts = shape_data.strip().split()
        if not parts:
            return None
        shape_type = parts[0]

        if shape_type == "Triangle" and len(parts) == 4:
            return Triangle(float(parts[1]), float(parts[2]), float(parts[3]))
        elif shape_type == "Rectangle" and len(parts) == 3:
            return Rectangle(float(parts[1]), float(parts[2]))
        elif shape_type == "Trapeze" and len(parts) == 5:
            return Trapeze(float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4]))
        elif shape_type == "Parallelogram" and len(parts) == 4:
            return Parallelogram(float(parts[1]), float(parts[2]), float(parts[3]))
        elif shape_type == "Circle" and len(parts) == 2:
            return Circle(float(parts[1]))
        else:
            print(f"Invalid shape data: {shape_data}")
            return None
    except ValueError as e:
        print(f"Error parsing shape data '{shape_data}': {e}")
        return None

def find_max_area_shape(shapes):
    if not shapes:
        return None
    max_shape = shapes[0]
    max_area = max_shape.area()
    for shape in shapes:
        if shape.area() > max_area:
            max_area = shape.area()
            max_shape = shape
    return max_shape

def find_max_perimeter_shape(shapes):
    if not shapes:
        return None
    max_shape = shapes[0]
    max_perimeter = max_shape.perimeter()
    for shape in shapes:
        if shape.perimeter() > max_perimeter:
            max_perimeter = shape.perimeter()
            max_shape = shape
    return max_shape

def process_file(file_path):
    shapes = []
    try:
        file = open(file_path, 'r')
        for line in file:
            shape = create_shape(line)
            if shape:
                shapes.append(shape)
        file.close()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return

    if not shapes:
        print(f"No valid shapes found in {file_path}")
        return

    max_area_shape = find_max_area_shape(shapes)
    max_perimeter_shape = find_max_perimeter_shape(shapes)

    print(f"Results for file {file_path}")
    print(f"Shape with maximum area: {max_area_shape}, Area: {round(max_area_shape.area(), 2)}")
    print(f"Shape with maximum perimeter: {max_perimeter_shape}, Perimeter: {round(max_perimeter_shape.perimeter(), 2)}")
    print()

def main():
    file_paths = ["input01.txt", "input02.txt", "input03.txt"]
    for file_path in file_paths:
        process_file(file_path)

if __name__ == "__main__":
    main()
