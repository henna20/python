def add(a, b):
    n = a + b
    print("Sum:", n)


def subtract(a, b):
    n = a - b
    print("Subtract:", n)


def multiply(a, b):
    n = a * b
    print("Multiply:", n)


def divide(a, b):
    n = a / b
    print("Divide:", int(n))


def remainder(a, b):
    n = a % b
    print("Remainder:", n)


a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

add(a, b)
subtract(a, b)
multiply(a, b)
divide(a, b)
remainder(a, b)
