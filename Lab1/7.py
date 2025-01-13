# Manipulate strings using various built-in functions.

text = "Hello, my name is Sujal Bhandari and I don't like Python, hail c++. "
length_of_string = len(text)
print(f"Length of the string: {length_of_string}")

uppercase_string = text.upper()
lowercase_string = text.lower()
print(f"Uppercase version: {uppercase_string}")
print(f"Lowercase version: {lowercase_string}")

substring = "Python"
is_substring_present = substring in text
print(f"Is '{substring}' present in the string? {is_substring_present}")

words_list = text.split()
print(f"List of words: {words_list}")
