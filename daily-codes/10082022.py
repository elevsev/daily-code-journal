# dunders 

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __add__(self, other):
        return Vector(self.x + other.x + self.y + other.y)

    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"

v1 = Vector(10, 20)
print(v1.x, v1.y)
v2 = Vector(50, 60)
print(v2.x, v2.y)
print(v1, v2)
# print(v3.x)
# print(v3.y)
# print(v3)