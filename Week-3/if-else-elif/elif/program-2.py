# Movie Ticket Price Calculation 

age = int(input("Enter your age: "))

if age < 5:
    print("Free Entry for Kids")
elif age < 18:
    print("Ticket Price: ₹150 (Child Ticket)")
elif age < 60:
    print("Ticket Price: ₹250 (Adult Ticket)")
else:
    print("Ticket Price: ₹120 (Senior Citizen Discount)")
