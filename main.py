import pytest
VOWELS = ['a', 'e', 'i', 'o', 'u', 'y', 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

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

def is_vowel(a):
    return a.lower() in VOWELS

def vowel_count(a):
    count = 0
    for char in a:
        if char in VOWELS:
            count += 1
    return count

@pytest.mark.parametrize("test_input, expected", [
    ("hello" ,2),
    ("world",1),
    ("aeiou", 5),
    ("Привет!", 2),
    ("Привет, мир!",3),
    ("Првт, мр! Кк дл?", 0),
])


def test_vowel_count(test_input, expected):
    assert vowel_count(test_input) == expected


