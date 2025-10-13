# Simple calculator basic on Python
# Command
# (+, -, *, / and then exit)

command = ""

# Loop until user enters "exit"
while command != "exit":
    # Get command from user
    command = input("Enter command: ")
    
    # Exit loop if command is "exit"
    if command == "exit":
        break
    
    # Check if command is valid
    if command != "+" and command != "-" and command != "*" and command != "/":
        print("Invalid command!")
        continue
    
    # Get two numbers from user
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    
    # Perform calculation
    if command == "+":
        result = x + y
    elif command == "-":
        result = x - y
    elif command == "*":
        result = x * y
    elif command == "/":
        # Check if y is zero
        if y == 0:
            print("Cannot divide by zero!")
            continue
        
        # Perform division
        result = x / y
    
    # Print result
    print("Result: " + str(result))
    
print("Goodbye! And have a nice day!")
