import math, sys

def add(a, b):
  return a+b


def subtract(a, b):
    """Subtract two numbers."""
    return a -b
    print("Subtraction done!")  


def multiply(a, b):
  return a * b

def divide(a, b):
    if b == 0:
        print("Cannot divide by zero!")
        return
    return a / b


result_add = add(5, 3)
print("Addition Result:",result_add)  
result_sub = subtract(10,5)
result_mul = multiply(4, 2)
result_div = divide(8, 2)

print("Subtraction Result:", result_sub)
print("Multiplication Result:", result_mul)
print("Division Result:", result_div)