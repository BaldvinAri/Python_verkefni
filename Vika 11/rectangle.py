class Rectangle(object):
    def __init__(self,length=1,width=1):
        if length > 0:
            self.__length = length
        else:
            self.__length = 1

        if width > 0:
            self.__width = width
        else:
            self.__width = 1
        

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return self.__length*2 + self.__width*2

    def __str__(self):
        return f"Length: {self.__length}, Width: {self.__width}"

    def __eq__(self,other):
        return self.area() == other.area()

    def __repr__(self):
        return f"Rectangle({self.__length},{self.__width})"


rec1 = Rectangle(10, 2)
rec2 = Rectangle(2, 10)
assert rec1.area() == 20
assert rec1.perimeter() == 24
assert rec2.area() == 20
assert rec2.perimeter() == 24
assert (rec1 == rec2) == True
rec3 = Rectangle(4, 5)
print(rec3.area())
assert rec3.area() == 20
assert rec3.perimeter() == 18
assert rec1 == rec3
assert (rec1 != rec3) == False
rec4 = Rectangle()
assert rec4.area() == 1
assert rec4.perimeter() == 4
assert (rec1 == rec4) == False
assert rec1 != rec4