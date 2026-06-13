# This code defines a function called `hello_guys` that takes two parameters: `name` and `age`. The function prints some messages to indicate that it is calculating the greeting message, and then it returns a formatted string that includes the name and age. Finally, the function is called with the arguments "Alice" and 30, and the result is printed.

def hello_guys(name, age):
    # This function takes a name and age as input and returns a greeting message.
    print("This function will return a greeting message.")
    return f"Hello {name}, you are {age} years old."

result = hello_guys("Alice", 30)
print(result)

# Second example of a function that returns a value. This function calculates multiplication of two numbers and returns the result.
def multiply(a, b):
    # This function takes two numbers and returns their product.
    print("Calculating the product of two numbers...")
    result = a * b
    return result

result = multiply(5, 4)
print(f"The product of 5 and 4 is: {result}")