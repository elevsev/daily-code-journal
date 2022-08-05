import math 

def area_of_a_circle(radius):
    a = math.pi * radius**2
    return a 

radii = [2, 4, 6, 8, 10]
for r in radii:
    print("Area of circle with radius of ", r,  " = ", area_of_a_circle(radius=r), "units sq.")