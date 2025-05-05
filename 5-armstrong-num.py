# 5. Print all Armstrong numbers in a range(100-999)


print("Armstrong numbers between 100 and 999:")
for num in range(100, 1000):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num)