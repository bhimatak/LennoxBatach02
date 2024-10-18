class Rectangle:

    def __init__(self, w,h):
        self._w = w
        self._h = h

    def area(self):
        return (self._w*self._h)

class Square(Rectangle):
    def __init__(self,s):
        super().__init__(s,s)
        # self._s = s

# class Circle(Square):
#     def __init__(self,s):
#         super(Circle, self).__init__(s)


r = Rectangle(3,4)
print(r.area())

s = Square(4)
print(s.area())

# c = Circle(5)
# c.area()