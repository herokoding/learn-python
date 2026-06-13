# Exception Handling in Python
# This code demonstrates how to handle exceptions in Python using a try-except block. It attempts to perform a division operation and catches the ZeroDivisionError if the user tries to divide by zero.
try:
    # Code that may raise an exception
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
    # If the user enters zero for num2, a ZeroDivisionError will be raised. If the user enters a non-integer value, a ValueError will be raised.
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
    # This block will execute if a ZeroDivisionError is raised.
except ValueError:
    print("Error: Please enter valid integers.")
    # This block will execute if a ValueError is raised.
# Another example of exception handling where we try to access an index that is out of range in a list.
my_list = [1, 2, 3]

try:
    # Attempting to access an index that is out of range
    print(my_list[5])
    # This will raise an IndexError since there is no index 5 in the list.
except IndexError:
    print("Error: Index out of range. Please check the list length.")
    
# A final example of handling multiple exceptions in a single try block. This code attempts to convert a string to an integer and then perform a division operation.

try:
    # Attempting to convert a string to an integer
    num = int(input("Enter a number: "))
    # Attempting to divide 100 by the input number
    result = 100 / num
    print(f"100 divided by {num} is: {result}")
except (ValueError, ZeroDivisionError):
    print("Error: Invalid input. Please enter a non-zero integer.")
    
# This code handles both ValueError and ZeroDivisionError exceptions.