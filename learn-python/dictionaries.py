# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates

thisDict = {
    "name":"daniyalali",
    "age":"19",
    "job":"programmer",
    "uni":"uok",
    "colors": ["js", "react", "python"]
}

print(thisDict)
print(thisDict["colors"][0])
print(thisDict["name"]) #return daniyalali
print(type(thisDict)) #return <class 'dict'>
print("thisDict key",thisDict.keys()) #return key
print("thisDict value",thisDict.values());
print("item",thisDict.items())
#change uni value
thisDict["uni"]="Iba"
print("update the uni value",thisDict)