# OPERATORS:
# + , - , * , / , % , //

print("Addition of two number is ",2+1)
print("Subtraction of two number is ",2-1)
print("Multiplication of two number is ",2*2)
print("Division of two number is ",4/2)
print("Modulus of two number is ",4%2)
print("Exponentiation of two number is ",6**2)
print("Floor division of two number is ",7%2)



# BOOLEAN OPERATOR
#  == , and , or , not
print("Euqal operator",1 == 0);
# LOGICAL OPERATOR
print("Not Equal",not 1 == 0)
print("And operaot",2==2 and 2==3)
print("OR operator",2==2 or 2==3)

# ASSIGNMENT OPERATOR:

numAdd = 8.0
numAdd +=2.5
print(numAdd)

numSub = 8.0
numSub -=2.5
print(numSub)

numMul = 8.0
numMul *=2.5
print(numMul)

# STRINGS:

# String Concatenation
print("Artificial intelligence" + "is the intelligence of machines");

#The len() function returns the length of a string
strLength = "Artificial intelligence";
print("The length of the string is:",len(strLength))

# To check if a certain phrase or character is present in a string, we can use the keyword in.(return boolean)

txt = "The best things in life are free!"
print("free" in txt)

# uppercase / lowercase
print("uppercase".upper())
print("LOWERCASE".lower())

# LIST

fruits = ['apple','orange','pear','banana']
print(fruits);
print("Access the Apple",fruits[0])
