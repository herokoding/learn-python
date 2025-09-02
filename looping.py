# Looping While
def print_numbers_while(n):
    i = 1
    while i <= n:
        print(i)
        i += 1
    return "Done"

# Test the function
print(print_numbers_while(5))

# Looping For
def print_numbers_for(n):
    for i in range(1, n + 1):
        print(i)
    return "Done"

# Test the function
print(print_numbers_for(5))

# More Examples Looping Any Situation
def print_numbers_skip(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            continue
        print(i)
    return "Done"

# Test the function
print(print_numbers_skip(5))

# Additional Examples Looping Any Situation
def print_numbers_reverse(n):
    for i in range(n, 0, -1):
        print(i)
    return "Done"

# Test the function
print(print_numbers_reverse(5))

# Looping With String Dummy Data Example
def print_characters(s):
    for char in s:
        print(char)
    return "Done"

# Test the function
print(print_characters("Hello"))