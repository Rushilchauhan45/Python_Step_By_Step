# pop : To Remove an item from a dictionary.
dict1 = {'a':'1','b':'2','c':'3'}
print("Original Dictionary:", dict1)
# Using pop() to remove an item
removed_item = dict1.pop('b')
print("After pop() :" , dict1)

# popitem : To remove the last inserted item from a dictionary.
# PopItem Works on LIFO Algorithm --> Last In First Out
dict2 = {'x':'10','y':'20','z':'30'}
print("Original Dictionary:", dict2)
# Using popitem() to remove the last inserted item
dict2.popitem()
print("After popitem() :", dict2)

# setdefault : To return the value of a key if it exists, otherwise insert the key with a specified value.
dict3 = {'a':10}
print("Original Dictionary:", dict3)
print("Set 'a' to Default :", dict3.setdefault('a',100))

# update : To update a dictionary with another dictionary or an iterable of key-value pairs.
dict4 = {'x':1, 'y':2}
dict5 = {'a':10, 'b':20}
print("Original Dictionary:", dict4)
print(dict4.update(dict5))
print("After update() :", dict4)