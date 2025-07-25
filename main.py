def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_even(a):
    return a % 2 == 0

def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b

