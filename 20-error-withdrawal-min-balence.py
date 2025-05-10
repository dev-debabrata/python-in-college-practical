# 20. Write a program to raise an error when the amount we withdraw from balance is lower than min balance 3000 


def withdraw(balance, amount):
    if balance - amount < 3000:
        raise ValueError("Withdrawal denied: balance below minimum limit")
    return balance - amount

try:
    print("New Balance:", withdraw(5000, 2500))
except ValueError as e:
    print(e)
