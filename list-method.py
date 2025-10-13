# List Method Python

numbers = [1, 2, 3, 4, 5]

# append adds an item to the end of the list
numbers.append(10)

# print all items in the list
print(numbers)

# insert adds an item at the specified index
# 4 is the index, 50 is the item
numbers.insert(4, 50)

print(numbers)

# pop removes an item at the specified index and returns it
numbers.pop(4)

print(numbers)

# remove removes the first occurrence of a specified item
numbers.remove(3)

print(numbers)

# sort sorts the list in ascending order
numbers.sort()

print(numbers)

# clear removes all items from the list
numbers.clear()

print(numbers)