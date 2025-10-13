# List Array Python

names = ["John", "Paul", "George", "Ringo"]

# print(names)
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[-1])
# print(names[1:2])

# Example using looping
for name in names:
    print(f"Name: {name}") # print name
    
# Example using enumerate
for index, name in enumerate(names):
    print(f"Index: {index}, Name: {name}")
    
# Example using while
index = 0
while index < len(names):
    print(f"Index: {index}, Name: {names[index]}")
    index += 1
    
# Example using while with enumerate
index = 0
while index < len(names):
    print(f"Index: {index}, Name: {names[index]}")
    index += 1
    
