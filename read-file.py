# Reading a File in Python

# This code demonstrates how to read a file in Python using the built-in open() function. It reads the contents of a file and prints it to the console.
# Open the file in read mode

# Open the file in read mode and ensure it is properly closed after reading
with open('example.txt', 'r') as file:
    # Read the contents of the file
    content = file.read()
    # Print the contents to the console
    print(content)
    
# Another example of reading a file line by line using a for loop
with open('example.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Print the current line
        print(line.strip())  # Using strip() to remove any leading/trailing whitespace
        
# A final example of reading a file and counting the number of lines it contains
line_count = 0
with open('example.txt', 'r') as file:
    # Iterate through each line in the file and count the lines
    for line in file:
        # Increment the line count
        line_count += 1
        # Print the current line
        print(f"The file contains {line_count} lines.")

# This code reads a file line by line using a for loop and prints each line to the console. It also counts the number of lines in the file and prints the total count at the end.

# Another examples with import csv module to read a CSV file
import csv

with open('example.csv', 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Print the current row
        print(row)