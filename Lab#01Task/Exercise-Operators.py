# Assignment Operators:
# Assignment operators are used to assign values to variables. Some common assignment operators include =, +=, -=, *=, /=, //=, %=, **=, etc.

numAdd = 8.0

numAdd +=2.5
print(numAdd)

numSub = 8.0
numSub -=2.5
print(numSub)

numMul = 8.0
numMul *=2.5
print(numMul)

# Logical Operators:
# Logical operators are used to combine conditional statements.

x = 6
y = 4

# Logical AND
print(x > 2 and y < 4)  

# Logical OR
print(x > 2 or y > 5)   

# Logical NOT
print(not(x > 2 and y < 4))

# Arithmetic Operators:
# Arithmetic operators are used to perform mathematical operations

print("Addition of two number is ",2+1)
print("Subtraction of two number is ",2-1)
print("Multiplication of two number is ",2*2)
print("Division of two number is ",4/2)
print("Modulus of two number is ",4%2)
print("Exponentiation of two number is ",6**2)

# Identity Operators:
# Identity operators are used to compare the memory locations of two objects.

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)    # Output: True
print(x is y)    # Output: False
print(x == y)    # Output: True

# Membership Operators:
# Membership operators are used to test if a sequence is presented in an object.

x = ["apple", "banana"]
print("banana" in x)    # Output: True
print("orange" not in x)    # Output: True

