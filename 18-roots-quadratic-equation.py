# 18. Find the roots of a quadratic equation using the math module 


import math

a, b, c = 1, -7, 12
d = b**2 - 4*a*c

if d >= 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("Roots:", root1, root2)
else:
    print("No real roots")