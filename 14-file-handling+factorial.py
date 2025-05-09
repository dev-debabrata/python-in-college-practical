# 14. Take a value from the user. Store it in a file and again read the value and Find the factorial of the number


num = int(input("Enter a number: "))
with open("data.txt", "w") as f:
    f.write(str(num))

with open("data.txt", "r") as f:
    num = int(f.read())

fact = 1
for i in range(1, num + 1):
    fact *= i

print("Factorial:", fact)
