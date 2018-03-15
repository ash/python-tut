class X:
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        return X(self.x + other.x)

x1 = X(5)
x2 = X(6)
x3 = x1 + x2
print(x3.x)
