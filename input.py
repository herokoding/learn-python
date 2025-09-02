# Taking user input for variables
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)


# More Examples Input
weight = float(input("Enter your weight in pounds: "))
is_male = input("Are you male? (yes/no): ").lower() == "yes"

print("Weight:", weight)
print("Is Male:", is_male)

# Expressing print with 2 or 3 variable input
print(f"Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}")

# Expressing calculations input age with this year
current_year = 2023
birth_year = current_year - age
print(f"Birth Year: {birth_year}")
print(f"My Age Now: {age}")
print(f"My Age Next Year: {age + 1}")