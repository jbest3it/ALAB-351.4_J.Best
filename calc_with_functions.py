# Write separate functions for each operation: add(a,b), subtract(a,b), multiply(a,b), divide(a,b) – each returning the result.
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Write a calculate(a, b, op) function that takes two numbers and a symbol for operation, and uses if/elif to call the correct operation function. 
def calculate(a, b, op):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    
# It should handle an invalid operation by returning or printing an error message.
    else:
        raise ValueError("Invalid operation. Please choose +, -, *, or /.")
    
# In the main program, ask the user for two numbers and an operation (just like before), but now use the calculate function to get the result and print it.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
op = input("Enter the operation (+, -, *, /): ")

try:
    result = calculate(a, b, op)
    print(f"The result is: {result}")
except ValueError as e:
    print(f"Error: {e}")