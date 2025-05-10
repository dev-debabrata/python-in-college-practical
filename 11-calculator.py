
# 11. Make a calculator with function with:
#                                             a) no return 
#                                             b) single return 

# a) no return 
def calc(a, b, op):
    if op == '+':
        print("Sum:", a + b)
    elif op == '-':
        print("Difference:", a - b)
    elif op == '*':
        print("Product:", a * b)
    elif op == '/':
        print("Quotient:", a / b)

calc(10, 5, '+')



# b) single return
def calc(a, b, op):
    return eval(f"{a}{op}{b}")

print("Result:", calc(10, 5, '*'))