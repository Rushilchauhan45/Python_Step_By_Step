#Membership Operation in String

str1 = "Hello World"
str2 = "Hellow"

# Using the 'in' operator to check membership
is_member = str2 in str1
print(is_member)  # Output: false
is_member1 = str1 not in str2
print(is_member1)  # Output: true