class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)

l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
r=rectangle(l,b)
y=r.area()
x=r.perimeter()
print("The area is:",y)
print("The perimeter is",x)

l2=int(input("Enter the length:"))
b2=int(input("Enter the breadth:"))
r2=rectangle(l2,b2)
y2=r2.area()
x2=r2.perimeter()
print("The area is:",y2)
print("The perimeter is",x2)

if y>y2:
    print("The 1st rectangle is greater then 2nd!!")
else:
    print("The 2nd rectangle is greater then 1st!!")