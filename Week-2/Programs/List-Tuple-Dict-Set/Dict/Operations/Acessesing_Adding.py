# ------------------------------------
# ✅ Accessing Elements from Dictionary
# ------------------------------------

# Creating a dictionary with company information
dict1 = {'Company':'Google','Slogan':'IT Consultansy Company','Since':'1998'}

# Accessing elements using square brackets []
# This method gets the value associated with the given key
print("Company Name:", dict1['Company'])
print("Company Slogan:", dict1['Slogan'])
print("Established Since:", dict1['Since'])

# Output:
# Company Name: Google
# Company Slogan: IT Consultansy Company
# Established Since: 1998


# ---------------------------
# ✅ Adding Elements to Dictionary
# ---------------------------

# Adding a new key-value pair to existing dictionary
# Syntax: dictionary_name['new_key'] = 'new_value'
dict1['Location'] = 'Mountain View, California'

# Print the updated dictionary
print("Updated Dictionary:", dict1)

# Output:
# Updated Dictionary: {'Company': 'Google', 'Slogan': 'IT Consultansy Company', 'Since': '1998', 'Location': 'Mountain View, California'}
