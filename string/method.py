name = "Kamla"

# First character
print("First character:", name[0])

# Last character
print("Last character:", name[-1])

# Length
print("Length:", len(name))

# Uppercase
print("Uppercase:", name.upper())

#Lowercase
print("Lowercase:", name.lower())


#🔹 1. strip() → Remove spaces
name = "  Kittu  "
print(name.strip())

#🔹 2. split() → Convert string to list
text = "apple banana mango"
print(text.split())

#🔹 3. join() → Convert list to string
words = ['Hello', 'Kittu']
print(" ".join(words))

#🔹 4. find() → Find position
name = "Kittu"
print(name.find("t"))

#🔹 5. count() → Count characters
name = "Kittu"
print(name.count("t"))

#🔹 6. startswith() → Check start
name = "Kittu"
print(name.startswith("t"))

#🔹 7. endswith() → Check end
name = "Kittu"
print(name.endswith("u"))

#🔹 8. isalpha() → Only letters?
name = "Kittu@"
print("Kittu".isalpha())

#🔹 9. isdigit() → Only numbers?
print("123".isdigit())

#🔹 10. capitalize() → First letter big
print("kittu".capitalize())