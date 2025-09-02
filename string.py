# String Manipulation Examples
name = "John"
greeting = f"Hello, {name}!"
print(greeting)

# More String Examples
quote = "The only limit to our realization of tomorrow is our doubts of today."
print("Quote:", quote)

# Demonstrating String Methods
print("Uppercase:", quote.upper())
print("Lowercase:", quote.lower())
print("Title Case:", quote.title())

# Demonstrating String Replacement
new_quote = quote.replace("doubts", "fears")
print("Replaced Quote:", new_quote)

# Demonstrating String Slicing
print("Sliced Quote (First 10 chars):", quote[:10])
print("Sliced Quote (Last 10 chars):", quote[-10:])

# String Functions
print("Length of Quote:", len(quote))
print("Count of 'o':", quote.count("o"))
