# If-Else Example
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Test the function
print(check_number(10))
print(check_number(-5))
print(check_number(0))

# More Examples If-Else Conditions Any Situation
def check_age(age):
    if age < 18:
        return "Minor"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

# Test the function
print(check_age(10))
print(check_age(30))
print(check_age(70))


# Additional Examples If-Else Conditions Any Situation
def check_temperature(temp):
    if temp > 30:
        return "Hot"
    elif temp > 20:
        return "Warm"
    else:
        return "Cold"

# Test the function
print(check_temperature(35))
print(check_temperature(25))
print(check_temperature(15))

# Use Operator Like != == > < >= <=
def check_value(x):
    if x != 10:
        return "Not Ten"
    elif x == 10:
        return "Ten"
    elif x > 10:
        return "Greater than Ten"
    else:
        return "Less than Ten"

# Test the function
print(check_value(10))
print(check_value(5))
print(check_value(15))
print(check_value(10))

# Use Operator Logical And Or Not
def check_logic(a, b):
    if a > 0 and b > 0:
        return "Both positive"
    elif a < 0 or b < 0:
        return "At least one negative"
    else:
        return "Both zero"

# Test the function
print(check_logic(10, 5))
print(check_logic(-10, 5))
print(check_logic(0, 0))

# Nested If-Else Conditions Any Situation
name = 'Herotomo Fazry'
by_pass_validation = False

if len(name) > 10 or by_pass_validation:
    print("Name is valid")
else:
    print("Name is invalid")