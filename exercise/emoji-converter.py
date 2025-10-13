# emoji converter from text to emoji on python

# simple exercise with dictionary on Python

# emoji converter from text to emoji on python

# simple exercise with dictionary on Python

# user input
sentence = input(">>> ")

# dictionary for emoji mapping
emoji_mapping = {
    ":)" : "😊",
    ":(" : "😢",
    ":D" : "😁",
    ":O" : "😲",
    ":P" : "😛",
    ":|" : "😐",
    ":/" : "😒",
}

# split user input into words
words = sentence.split(" ")

# create output string
output = ""

# loop over words and replace with emoji
for w in words:
    output += emoji_mapping.get(w, w) + " "

print(output)