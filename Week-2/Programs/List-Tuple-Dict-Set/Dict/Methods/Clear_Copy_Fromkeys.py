# Clear : Remove All items from the dictionary
dict1 = {'Movie':'Pushpa-2','Hero':'Allu Arjun','Heroin':'Rashmika Mandana','Villan':'Fahad Fasil','Description':'SandalWoods Smuggler','Release year':'2024'}
dict1.clear()
print("After clear:", dict1)
# Output: After clear: {}

# Copy : Return a shallow copy of the dictionary
dist2 = dict1.copy()
print("After copy:", dist2)
# Output: After copy: {} bcz dict1 is empty

# Fromkeys : Create a new dictionary with keys from the given sequence and values set to a specified value
keys = ['City' , 'Weather', 'Temperature']
dict3 = dict.fromkeys(keys, 'Unknown')
dict3['City'] = 'Bangalore'
dict3['Weather'] = 'Sunny'
dict3['Temperature'] = '30C'
print("Fromkeys:", dict3)