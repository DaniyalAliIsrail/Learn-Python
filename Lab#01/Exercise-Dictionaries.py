# Exercise: Dictionaries 
# (i)Use dir and help to learn about the functions you can call on dictionaries and implement it
# Implementing some dictionary functions

my_dict = {'a': "javascript", 'b': "python", 'c': "dart"}

#Adding an item from the dictionary
my_dict['d'] = "c++"
print(my_dict)

# Removing an item from the dictionary
del my_dict['c']
print(my_dict)

# Getting a list of keys
keys = my_dict.keys()
print(keys)

# Getting a list of values
values = my_dict.values()
print(values)

# Checking if a key exists in the dictionary
if "a" in my_dict:
    print("keys exsist")
else:
    print("key does not keys")    
    
# Checking if a key exists in the dictionary
value1 =my_dict.get("a")
print("value is associated with keys : ",value1)

# (ii)Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

finalDict = {**dic1,**dic2,**dic3}
print(finalDict)









