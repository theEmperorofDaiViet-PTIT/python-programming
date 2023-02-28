class Rectangle:
    def __init__(self, length, width, Color):
        self.length = length
        self.width = width
        self.Color = Color

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def color(self):
        return self.Color.title()

arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
if r.length > 0 and r.width > 0:
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))    	
else:
   	print("INVALID")