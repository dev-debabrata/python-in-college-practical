# 10.
# a)print multiplication table of number using user input 
# b) print the factors of a number.


# a)print multiplication table of number using user input 
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")


# b) print the factors of a number.
num = int(input("Enter a number: "))
print("Factors are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
