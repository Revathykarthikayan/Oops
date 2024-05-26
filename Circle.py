class Circle:

    def __init__(self, radius,pi=3.14):
        self.radius = radius
        self.pi = pi

    def area(self):
        return  self.pi *(self.radius**2)

    def peri(self):
        return  (2 * self.pi) * self.radius


c1 = Circle(10)
print(f"Area of circle with radius {c1.radius} is",c1.area())
print(f"Perimeter of circle with radius {c1.radius} is",c1.peri())
print()

c2 = Circle(22)
print(f"Area of circle with radius {c2.radius} is",c2.area())
print(f"Perimeter of circle with radius {c2.radius}  is",c2.peri())
print()

c3 = Circle(87)
print(f"Area of circle with radius {c3.radius} is",c3.area())
print(f"Perimeter of circle with radius {c3.radius} is",c3.peri())
print()

c4 = Circle(100)
print(f"Area of circle with radius {c4.radius} is",c4.area())
print(f"Perimeter of circle with radius {c4.radius} is",c4.peri())
print()

c5 = Circle(999)
print(f"Area of circle with radius {c5.radius} is",c5.area())
print(f"Perimeter of circle with radius {c5.radius} is",c5.peri())
print()

c6 = Circle(351)
print(f"Area of circle with radius {c6.radius} is",c6.area())
print(f"Perimeter of circle with radius {c6.radius} is",c6.peri())
print()

c7 = Circle(501)
print(f"Area of circle with radius {c7.radius} is",c7.area())
print(f"Perimeter of circle with radius {c7.radius} is",c7.peri())
print()


c8 = Circle(37)
print(f"Area of circle with radius {c8.radius} is",c8.area())
print(f"Perimeter of circle with radius {c8.radius} is",c8.peri())
