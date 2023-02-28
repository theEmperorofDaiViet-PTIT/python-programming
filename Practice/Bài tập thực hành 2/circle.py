class Circle():
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def describe_circle(self):
        print(f"The circle with center O{self.center} and radius R={self.radius}")
    def get_area(self):
        return (self.radius**2)*3.14
    def get_premiter(self):
        return 2*3.14*self.radius

circle = Circle((3,4), 7)
circle.describe_circle()
print(circle.get_area())