#TypeCasting Means Conversion Of Data In One Type To Other Type....


#For example:
# 🔹 int() – to convert string/float to integer

print(int("5"))     # 5
print(int(4.9))     # 4

# 🔹 float() – to get decimal

print(float("3.14"))  # 3.14
print(float(5))       # 5.0

# 🔹 str() – to convert any data type to string

a = 100
print("Value is: " + str(a))

# 🔹 bool() – to convert any data type to boolea

print(bool(""))       # False
print(bool("Rushil")) # True

# if you wanna check the type of variable you can use "type()" function

'''
+--------------+----------------+--------------+--------+--------+
| From → To    | int()          | float()      | str()  | bool() |
+--------------+----------------+--------------+--------+--------+
| str          | ✅ if numeric  | ✅if numeric| ✅     | ✅   |
| int          | ✅             | ✅          | ✅     | ✅   |
| float        | ✅             | ✅          | ✅     | ✅   |
| bool         | ✅             | ✅          | ✅     | ✅   |
+--------------+----------------+--------------+--------+--------+
'''


'''
----------------------------------------------------------------------------------------
| Function      | Converts TO    | Example Usage                         | Output Type |
| ------------- | -------------- | ------------------------------------- | ----------- |
| `int()`       | Integer        | `int("10")`, `int(3.9)`               | `int`       |
| `float()`     | Float          | `float("3.14")`, `float(5)`           | `float`     |
| `str()`       | String         | `str(100)`, `str(True)`               | `str`       |
| `bool()`      | Boolean        | `bool(1)`, `bool("hello")`, `bool(0)` | `bool`      |
----------------------------------------------------------------------------------------
| `list()`      | List           | `list("abc")`, `list((1,2,3))`        | `list`      |
| `tuple()`     | Tuple          | `tuple("abc")`, `tuple([1,2,3])`      | `tuple`     |
| `set()`       | Set            | `set("hello")`, `set([1,1,2,3])`      | `set`       |
| `dict()`      | Dictionary     | `dict([("a",1), ("b",2)])`            | `dict`      |
----------------------------------------------------------------------------------------
| `complex()`   | Complex number | `complex(2, 3)`                       | `complex`   |
| `bytes()`     | Bytes          | `bytes("abc", "utf-8")`               | `bytes`     |
| `bytearray()` | Byte array     | `bytearray("abc", "utf-8")`           | `bytearray` |
| `frozenset()` | Immutable set  | `frozenset([1,2,3])`                  | `frozenset` |
----------------------------------------------------------------------------------------


'''