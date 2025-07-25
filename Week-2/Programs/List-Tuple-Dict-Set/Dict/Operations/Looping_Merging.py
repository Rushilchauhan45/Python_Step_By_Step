# ---------------------------
# ✅ Looping in Dictionaries
# ---------------------------

# Creating a cricket-themed dictionary
dict1 = {'captain':'Rohit_sharma','fast_bowler':'jasprit_bumrah','venue':'eden_gardens'}

# Looping through dictionary keys and accessing their values
# The for loop iterates over each key in the dictionary
for key in dict1:
    print(key, ':', dict1[key])

# Output:
# captain : Rohit_sharma
# fast_bowler : jasprit_bumrah
# venue : eden_gardens


# ---------------------------
# ✅ Merging Two Dictionaries
# ---------------------------

# Creating two separate dictionaries - one for bike and one for car
bike_dict = {'brand':'yamaha','model':'r15_v4','price':'180000'}
car_dict = {'manufacturer':'toyota','model':'fortuner','body_type':'suv'}

# Method 1: Using unpacking operator (**)
# This method unpacks both dictionaries and creates a new merged dictionary
merge_dict = {**bike_dict, **car_dict}
print("Merged using ** operator:", merge_dict)

# Method 2: Using pipe operator (|) - Available in Python 3.9+
# This is a newer syntax for merging dictionaries
merge_dict2 = bike_dict | car_dict
print("Merged using | operator:", merge_dict2)

# Output:
# Merged using ** operator: {'brand': 'yamaha', 'model': 'fortuner', 'price': '180000', 'manufacturer': 'toyota', 'body_type': 'suv'}
# Merged using | operator: {'brand': 'yamaha', 'model': 'fortuner', 'price': '180000', 'manufacturer': 'toyota', 'body_type': 'suv'}
