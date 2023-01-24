class Rectangle():
    def __init__(self):
        self._l = int(input("Enter the Length: "))
        self._b = int(input("Enter the Breadth: "))
        self.area = self._l *  self._b

    def greaterThan(self,Rectangle):
        if self.area < Rectangle.area:
            print("Area of Object 1 is Greater")
        else:
            print("Area of Object 2 is Greater")

print("Object 1: ")
o1 = Rectangle()
print("Object 2: ")
o2 = Rectangle()
print("Comparing Objects: ")
o2.greaterThan(o1)