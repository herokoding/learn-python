# Tutorial List Summary Python
# List Summary Python

# Declare a list of numbers
numbers = [5, 6, 7, 8, 2]

# Initialize variable
init_number = 0

# Looping the list
for number in numbers:
    # Add each number to the variable
    init_number = init_number + number
    
print(init_number)


# Get the maximum number from the list
max_number = numbers[0]

# Looping the list to compare each number
for number in numbers:
    # If the current number is more than the max number
    if number > max_number:
        # Replace the max number with the current number
        max_number = number
        
print(max_number)