# Simple exercise with dictionary on Python

# Start with input numbers and return string
# Example : 1 = one, 2 = two, 3 = three, etc.
# Input : [1,2,3,4,5,6,7,8,9,10]
# Output : {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten'}

numbers = input("Enter number : ")

# mapping between number and string
mapping_number = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    "10" : "ten",
    "11" : "eleven",
    "12" : "twelve",
}

# placeholder for output
output = ""

# iterate through the input numbers
for n in numbers:
    # get the string representation of number
    terbilang = mapping_number.get(n, "Invalid number")
    
    # append to output
    output = output + terbilang + " "

print(output)

# or use dictionary comprehension
# output = {n : mapping_number.get(n, "Invalid number") for n in numbers}
# print(output)

# if multiple input with split
numbers = input("Enter number : ").split(",")
output = {mapping_number.get(n, "Invalid number") for n in numbers}
print(output)

# if numbers 10 (ten) and above like 10 - 100
# example when input 10 return string "ten"
# numbers = input("Enter number : ")
# output = {mapping_number.get(str(i), "Invalid number") for i in range(1, int(numbers) + 1)}
# print(output)