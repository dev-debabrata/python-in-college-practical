# 17. Calculate the area of a triangle, square and rectangle using a user defined function 


def area_triangle(base, height):
    return 0.5 * base * height

def area_square(side):
    return side * side

def area_rectangle(length, width):
    return length * width

print("Triangle:", area_triangle(5, 4))
print("Square:", area_square(4))
print("Rectangle:", area_rectangle(5, 3))
