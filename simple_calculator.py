# ask user to input two numbers. convert from strings to integers (or floats) as needed.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# checks if digit was inputted using isdigit.
 #  num1.isdigit() and num2.isdigit(): 
 #  print("Invalid input. Please enter valid numbers.")
 #   exit()

# ask the user to choose an operation 
operation = input("Choose an operation (+, -, *, /): ")

# perform the chosen operation on the two numbers.
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2

# makes sure only valid operations are performed.
else:
    print("Invalid operation. Please choose +, -, *, or /.")
    result = None

# print the result in a user-friendly way
if result is not None:
    print(f"{num1} {operation} {num2} = {result}")

