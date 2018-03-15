class Shape:
    def draw(self):
        print('Drawing a Shape')

class Circle(Shape):
    def draw(self):
        print('Drawing a Circle')

class Square(Shape):
    def draw(self):
        print('Drawing a Square')

class Triangle(Shape):
    def draw(self):
        print('Drawing a Triangle')

shapes = []
shapes.append(Circle())
shapes.append(Circle())
shapes.append(Square())
shapes.append(Triangle())
shapes.append(Square())
shapes.append(Triangle())

for s in shapes:
    s.draw()
