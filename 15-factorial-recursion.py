# 15. Calculate factorial using recursion method 


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))
