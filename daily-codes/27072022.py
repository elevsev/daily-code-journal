class Shapes:
    '''
    This class is used to create a shape object.
    '''
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        '''
        Calculates the area of a square-like shape.
        '''
        area = self.length * self.breadth
        return area

square = Shapes(length=3, breadth=3)
print(f"This is the Shapes class as an object: {square}")
print(f"This is the area of the square: {square.area()}sq.")
