# 19. Calculate the area of a circle and triangle using the math module 


import math

def circle_area(radius):
    return math.pi * radius ** 2

def triangle_area(base, height):
    return 0.5 * base * height

print("Circle:", circle_area(5))
print("Triangle:", triangle_area(4, 6))
