# Examples
from ast import Import
import math



def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
    if b != 0:
        result = a / b
        return result
    else:
        return "Division by zero error"

def power(a, b):
    result = a ** b
    return result

# More Examples
def modulus(a, b):
    result = a % b
    return result

def floor_division(a, b):
    result = a // b
    return result

# Additional Examples
def square(a):
    result = a * a
    return result

def cube(a):
    result = a * a * a
    return result

# More Additional Examples
def fourth_power(a):
    result = a ** 4
    return result

def fifth_power(a):
    result = a ** 5
    return result


# Call each function and print the result
print(add(3, 4))
print(subtract(3, 4))
print(multiply(3, 4))
print(divide(3, 4))
print(power(3, 4))
print(modulus(3, 4))
print(floor_division(3, 4))
print(square(3))
print(cube(3))
print(fourth_power(3))
print(fifth_power(3))
