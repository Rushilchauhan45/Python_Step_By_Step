# ----------------------------
# ✅ Dictionary Comprehension
# ----------------------------

# This line creates a dictionary where:
# - Keys are numbers from 1 to 9
# - Values are squares of the keys (X * X)
dict1 = { X : X*X for X in range(1, 10) }

# Print Output the dictionary
print("Square Dictionary:", dict1)

# Output:
# Square Dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}


# ------------------------------------------
# ✅ Converting Two Lists into a Dictionary
# ------------------------------------------

# List of keys
list_key = ['a', 'b', 'c', 'd']

# List of values
list_value = [1, 2, 3, 4]

# The zip() function pairs each key with its corresponding value
# dict() converts the zipped object into a dictionary
dic1 = dict(zip(list_key, list_value))

# Print Output the new dictionary
print("List to Dictionary:", dic1)

# Output:
# List to Dictionary: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
