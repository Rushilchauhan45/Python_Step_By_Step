#Acess any index From set
# We Have Builting Function for Convert Any Data Structure to Set --> set(object)
# But We Can't Access Any Index From Set Because Set is Unordered Collection

#1st Making way of Set
set1 = {1, 2, 3, 4, 5} #Default Making way Of Set 

#2nd Making way of Set
set2 = set([1,2,3,4,5]) # Converting List to Set
set3 = set((1, 2, 3, 4, 5)) # Converting Tuple to Set

#3rd Making way of Set
set4 = set("Python") # set= {"p" , "y", "t", "h", "o", "n"}  Converting String to Set

#4th Making way of Set
set5 = set() #Empty Set

print(set1)
print(set2)
print(set3)
print(set4)
print(set5)



