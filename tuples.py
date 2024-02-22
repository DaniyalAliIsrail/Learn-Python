# TUPLE
# TUPLES ARE USED TO STORE MULTIPLE ITEMS IN A SINGLE VARIABLE 

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple);

#CHECK THE TYPE OF TUPLES
thistupleTypecheck = ("apple",)
print("type of ",type(thistupleTypecheck)) #output class is tuple

#NOT A TUPLE
thistupleType = ("apple") #One item tuple , remember the comma
print(type(thistupleType )) #output class is string

#TUPLE ALLOW DUPLICATE VALUES 
thistuple1 = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple1)
print("length of tuple",len(thistuple1))


# A TUPLE WITH STRING, INTEGERS AND BOOLEAN VALUES:
strIntBoll = ("abc", 34, True, 40, "male")
print(type(strIntBoll))

#ACCESS THE TUPLE THE ITEM
print("Access the tuples index 0 to length of the tuple" ,thistuple1[0:])
print("Access the last element of the tuple",thistuple1[-1])
print("Access the desire tuple item",thistuple1[2:5])

