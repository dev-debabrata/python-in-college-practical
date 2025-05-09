# 12. Write a program to make three function blocks which show uppercase,lowercase and numbers when called. Show the characters using their ASCII value


def show_uppercase():
    for i in range(65, 91):
        print(chr(i), end=' ')
    print()

def show_lowercase():
    for i in range(97, 123):
        print(chr(i), end=' ')
    print()

def show_numbers():
    for i in range(48, 58):
        print(chr(i), end=' ')
    print()

show_uppercase()
show_lowercase()
show_numbers()
