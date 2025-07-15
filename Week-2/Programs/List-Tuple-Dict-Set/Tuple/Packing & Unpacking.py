#what is Packing And Unpacking In Tuple ?


# Packing : Assigning multiple values to a single variable
tuple1 = (1, 2.34, "Hello", 4000000000, 5.83294829429289, True)
print("Packing:",tuple1)


# Unpacking : Assigning values from a tuple to multiple variables
tuple2 = ("John Deo" , 25 , "New York" , "9874421234")

name , age , city , phone = tuple2
print("Name: ",name)
print("Age: ",age)
print("City: ",city)
print("Phone: ",phone)
