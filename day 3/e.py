# Write a Python program that uses a set comprehension to extract all unique alphabetic
# characters from a given string, ignoring case.

text = "Hello World!"
unique_characters={char.lower() for char in text if char.isalpha()}
# sorted_characters=sorted(unique_characters)
print(unique_characters)