# Define a function greet_user() that takes a name (string) as a parameter and prints a greeting, e.g., "Hello, <name>! Welcome!". 
def greet_user(name):
    if name:
        print(f"Hello, {name}! Welcome!")
# If no name is provided (you can simulate this by calling greet_user() with an empty string or by using a default parameter value), 
# it should print "Hello! Welcome!".
    else:
        print("Hello! Welcome!")

# Define a function add_two_numbers(a, b) that returns the sum of two numbers a and b.
def add_two_numbers(a, b):
    return a + b

# Define a function is_even(num) that returns True if num is even or False otherwise.
def is_even(num):
    return num % 2 == 0

# In the main part of the script (outside the functions), demonstrate each function:
# Call greet_user() with a sample name and without a name.
greet_user("Tina")
greet_user("")
# Call add_two_numbers() with two numbers, print the result.
add_two_numbers(3, 9)
print(f"The sum of 3 and 9 is: {add_two_numbers(3, 9)}")
# Call is_even() on a couple of numbers (one even, one odd) and print the results in a descriptive way (e.g., "4 is even: True").
print(f"4 is even: {is_even(4)}")
print(f"5 is even: {is_even(5)}")
