# get : To get Specific Key Value
dict1 = {'a':'100','b':'200','c':'300','d':'400'}
print(dict1.get('a'))  # Output: 100
print(dict1['a'])  # Output: 100

# items : To get all Key Value Pairs
print(dict1.items())
# Output: dict_items([('a', '100'), ('b', '200'), ('c', '300'), ('d', '400')])

#keys : To get all Keys
print(dict1.keys())
# Output: dict_keys(['a', 'b', 'c', 'd'])

# values : To get all Values
print(dict1.values())
# Output: dict_values(['100', '200', '300', '400'])
