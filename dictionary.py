# Tutorial Dictionary Python
# Dictionary Python

# Declare a dictionary
# A dictionary is a collection of key-value pairs.
# It is unordered and indexed.
# It is mutable, meaning that it can be changed.
# It is written with curly brackets and consists of key-value pairs.
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Print the dictionary
print(my_dict)

# Or use the dict() function
my_dict = dict(name="John", age=30, city="New York")
print(my_dict)

# Or use the dict() function with a list of tuples
my_dict = dict([("name", "John"), ("age", 30), ("city", "New York")])
print(my_dict)

# Or using get to access each value
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict.get("name"))
print(my_dict.get("age"))
print(my_dict.get("city"))
print(my_dict.get("country")) # Output: None (because key not found)