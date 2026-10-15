# A function safe_divide(a, b) that returns the result of a / b if b is not zero.
def safe_divide(a, b):
    # If b is zero, the function should raise a ValueError with a message “Cannot divide by zero”.
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Use a try/except structure to call safe_divide with some test values that include a zero divisor. 
try:
    result = safe_divide(10, 0)
    print(f"The result is: {result}")

# Catch the ValueError and print an error message to the user.
except ValueError as e:
    print(f"Error: {e}")

# Include a finally clause in the try/except that prints a message like “Division operation completed” whether or not an error occurred.
finally:
    print("Division operation completed.")

# Also demonstrate catching a generic exception by performing an unsafe operation (for example, converting an invalid string to int in a try block) and... 
# Catch the generic Exception to print a message.
try:
    invalid_number = int("invalid")
    print(f"The converted number is: {invalid_number}")
except Exception as e:
    print(f"An error occurred: {e}")