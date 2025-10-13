# Tutorial Unpack Python
# Unpack Python

# Definition: Unpack is a process of taking a single value and breaking it down into multiple values.

# Declare a tuple of numbers
numbers = (5, 6, 7, 8, 2)

# Unpack the tuple into variables
a, b, c, d, e = numbers

# Print the variables
print(a)  # Output: 5
print(b)  # Output: 6
print(c)  # Output: 7
print(d)  # Output: 8
print(e)  # Output: 2

# Or use the * operator to unpack the tuple into a list
numbers = (5, 6, 7, 8, 2)
a, *b = numbers
print(a)  # Output: 5
print(b)  # Output: [6, 7, 8, 2]