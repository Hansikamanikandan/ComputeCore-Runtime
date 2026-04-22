def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Sum:", add(a, b))
print("Difference:", subtract(a, b))
print("Product:", multiply(a, b))
print("Quotient:", divide(a, b))
