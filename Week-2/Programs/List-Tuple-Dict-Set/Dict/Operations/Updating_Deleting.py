# --------------------------------
# ✅ Updating Elements in Dictionary
# --------------------------------

# Creating a dictionary with college information
dict1 = {'College':'GEC,Sector-28 ','Principle':'Dr. J . M . rathod','Department':'E & C','batch':'A1'}

# Updating an existing key's value
# Syntax: dictionary_name['existing_key'] = 'new_value'
dict1['Principle'] = 'Dr. Nisarg Bhatt'

# Print the updated dictionary
print("After updating Principle:", dict1)

# Output:
# After updating Principle: {'College': 'GEC,Sector-28 ', 'Principle': 'Dr. Nisarg Bhatt', 'Department': 'E & C', 'batch': 'A1'}


# --------------------------------
# ✅ Deleting Elements from Dictionary
# --------------------------------

# Using del keyword to remove a key-value pair
# Syntax: del dictionary_name['key_to_delete']
del dict1['batch']

# Print the dictionary after deletion
print("After deleting batch:", dict1)

# Output:
# After deleting batch: {'College': 'GEC,Sector-28 ', 'Principle': 'Dr. Nisarg Bhatt', 'Department': 'E & C'}
